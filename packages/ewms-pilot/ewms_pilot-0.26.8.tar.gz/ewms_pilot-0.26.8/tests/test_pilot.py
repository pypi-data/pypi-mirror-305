"""Test pilot submodule."""

import asyncio
import base64
import json
import logging
import os
import pickle
import re
import time
from datetime import date, timedelta
from pprint import pprint
from typing import List, Optional
from unittest.mock import patch

import asyncstdlib as asl
import mqclient as mq
import pytest

from ewms_pilot import ContainerRunError, config, consume_and_reply
from ewms_pilot.config import ENV, PILOT_DATA_DIR, PILOT_DATA_HUB_DIR_NAME

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("mqclient").setLevel(logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)


TIMEOUT_INCOMING = 3

MSGS_TO_SUBPROC = ["item" + str(i) for i in range(30)]


@pytest.fixture
def queue_incoming() -> str:
    """Get the name of a queue for talking to client(s)."""
    return mq.Queue.make_name()


@pytest.fixture
def queue_outgoing() -> str:
    """Get the name of a queue for talking "from" client(s)."""
    return mq.Queue.make_name()


async def populate_queue(
    queue_incoming: str,
    msgs_to_subproc: list,
    intermittent_sleep: float,
) -> None:
    """Send messages to queue."""
    to_client_q = mq.Queue(
        config.ENV.EWMS_PILOT_QUEUE_INCOMING_BROKER_TYPE,
        address=config.ENV.EWMS_PILOT_QUEUE_INCOMING_BROKER_ADDRESS,
        name=queue_incoming,
    )

    async with to_client_q.open_pub() as pub:
        for i, msg in enumerate(msgs_to_subproc):
            if i and i % 2 == 0:  # add some chaos -- make the queue not saturated
                await asyncio.sleep(intermittent_sleep)
            else:
                await asyncio.sleep(0)  # for consistency
            await pub.send(msg)

    assert i + 1 == len(msgs_to_subproc)


async def assert_results(
    queue_outgoing: str,
    msgs_expected: list,
) -> None:
    """Get messages and assert against expected results."""
    from_client_q = mq.Queue(
        config.ENV.EWMS_PILOT_QUEUE_OUTGOING_BROKER_TYPE,
        address=config.ENV.EWMS_PILOT_QUEUE_OUTGOING_BROKER_ADDRESS,
        name=queue_outgoing,
    )
    received: list = []
    async with from_client_q.open_sub() as sub:
        async for i, msg in asl.enumerate(sub):
            print(f"{i}: {msg}")
            received.append(msg)

    assert len(received) == len(msgs_expected)

    # check each entry (special handling for dict-types b/c not hashable)
    if msgs_expected and isinstance(msgs_expected[0], dict):
        assert set(str(r) for r in received) == set(str(m) for m in msgs_expected)
    else:
        assert set(received) == set(msgs_expected)


def assert_pilot_dirs(
    n_tasks: int,
    task_dir_contents: List[str],
    data_hub_dir_contents: Optional[List[str]] = None,
    has_init_cmd_subdir: bool = False,
) -> None:
    """Assert the contents of the debug directory."""
    pprint(list(PILOT_DATA_DIR.rglob("*")))  # for debugging

    # validate args
    task_dir_contents = [c.rstrip("/") for c in task_dir_contents]
    assert len(task_dir_contents) == len(set(task_dir_contents))  # no duplicates
    #
    if not data_hub_dir_contents:
        data_hub_dir_contents = []

    # check num of dirs
    if has_init_cmd_subdir:
        assert (
            len(list(PILOT_DATA_DIR.iterdir())) == n_tasks + 1 + 1
        )  # data-hub/ & init*/
    else:
        assert len(list(PILOT_DATA_DIR.iterdir())) == n_tasks + 1  # data-hub/

    # check each task's dir contents
    for subdir in PILOT_DATA_DIR.iterdir():
        assert subdir.is_dir()

        # is this the data-hub subdir?
        if subdir.name == "data-hub":
            assert sorted(
                str(p.relative_to(subdir)) for p in subdir.rglob("*")
            ) == sorted(data_hub_dir_contents)
            continue
        # is this an init subdir?
        elif has_init_cmd_subdir and subdir.name.startswith("init"):
            assert sorted(
                str(p.relative_to(subdir)) for p in subdir.rglob("*")
            ) == sorted(["outputs/stderrfile", "outputs/stdoutfile", "outputs"])
            continue
        # now we know this is a task dir
        else:
            task_id = subdir.name

            # look at files -- flattened tree
            this_task_files = [f.replace("{UUID}", task_id) for f in task_dir_contents]
            assert sorted(this_task_files) == sorted(
                str(p.relative_to(subdir)) for p in subdir.rglob("*")
            )


########################################################################################
# SPECIAL (SLOW) TESTS -- RAN FIRST SO WHEN TESTS ARE PARALLELIZED, THINGS GO FASTER
########################################################################################


TEST_1000_SLEEP = 150.0  # anything lower doesn't upset rabbitmq enough


@pytest.mark.skipif(
    config.ENV.EWMS_PILOT_QUEUE_INCOMING_BROKER_TYPE != "rabbitmq",
    reason="test is only for rabbitmq tests",
)
@pytest.mark.parametrize(
    "refresh_interval_rabbitmq_heartbeat_interval",
    [
        # note -- the broker hb timeout is ~1 min and is triggered after ~2x
        TEST_1000_SLEEP * 10,  # won't actually wait this long
        TEST_1000_SLEEP,  # ~= to ~2x (see above)
        TEST_1000_SLEEP / 10,  # will have no hb issues
    ],
)
async def test_1000__heartbeat_workaround__rabbitmq_only(
    queue_incoming: str,
    queue_outgoing: str,
    refresh_interval_rabbitmq_heartbeat_interval: float,
) -> None:
    await _test_1000__heartbeat_workaround__rabbitmq_only(
        queue_incoming,
        queue_outgoing,
        refresh_interval_rabbitmq_heartbeat_interval,
    )


########################################################################################
# REGULAR TESTS
########################################################################################


@pytest.mark.parametrize(
    "image_envvar",
    [
        "CI_TEST_ALPINE_PYTHON_IMAGE",
        pytest.param(
            "CI_TEST_ALPINE_PYTHON_IMAGE_APPTAINER_SIF",
            marks=pytest.mark.skipif(
                ENV._EWMS_PILOT_CONTAINER_PLATFORM != "apptainer",
                reason="test only for apptainer",
            ),
        ),
        pytest.param(
            "CI_TEST_ALPINE_PYTHON_IMAGE_APPTAINER_FROM_DOCKER",
            marks=pytest.mark.skipif(
                ENV._EWMS_PILOT_CONTAINER_PLATFORM != "apptainer",
                reason="test only for apptainer",
            ),
        ),
    ],
)
async def test_000(
    image_envvar: str,
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            os.environ[image_envvar],
            """python3 -c "
output = open('{{INFILE}}').read().strip() * 2;
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


async def test_001__txt__str_filetype(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal .txt-based pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
output = open('{{INFILE}}').read().strip() * 2;
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            infile_ext=".txt",
            outfile_ext=".txt",
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.txt",
            "task-io/outfile-{UUID}.txt",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


async def test_100__json__objects(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal (object in, object out) .json-based pilot."""

    # some messages that would make sense json'ing
    msgs_to_subproc = [{"attr-0": v} for v in MSGS_TO_SUBPROC]
    msgs_outgoing_expected = [{"attr-a": v, "attr-b": v + v} for v in MSGS_TO_SUBPROC]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import json;
input=json.load(open('{{INFILE}}'));
v=input['attr-0'];
output={'attr-a':v, 'attr-b':v+v};
json.dump(output, open('{{OUTFILE}}','w'))" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            infile_ext=".json",
            outfile_ext=".json",
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.json",
            "task-io/outfile-{UUID}.json",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


async def test_101__json__preserialized(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a preserialized (json-string in, object out) .json-based pilot."""

    # some messages that would make sense json'ing
    msgs_to_subproc = [json.dumps({"attr-0": v}) for v in MSGS_TO_SUBPROC]
    msgs_outgoing_expected = [{"attr-a": v, "attr-b": v + v} for v in MSGS_TO_SUBPROC]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import json;
input=json.load(open('{{INFILE}}'));
v=input['attr-0'];
output={'attr-a':v, 'attr-b':v+v};
json.dump(output, open('{{OUTFILE}}','w'))" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            infile_ext=".json",
            outfile_ext=".json",
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.json",
            "task-io/outfile-{UUID}.json",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


async def test_200__pkl_b64(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a user-defined pickle/b64-based pilot."""

    dumps = lambda x: base64.b64encode(pickle.dumps(x)).decode()  # noqa: E731
    loads = lambda x: pickle.loads(base64.b64decode(x))  # noqa: E731

    # some messages that would make sense pickling
    msgs_to_subproc = [
        dumps(
            date(
                1995 + int(re.sub(r"[^0-9]", "", x)),
                int(re.sub(r"[^0-9]", "", x)) % 12 + 1,
                int(re.sub(r"[^0-9]", "", x)) % 28 + 1,
            )
        )
        for x in MSGS_TO_SUBPROC
    ]
    msgs_outgoing_expected = [
        dumps(loads(d) + timedelta(days=1)) for d in msgs_to_subproc
    ]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import pickle, base64;
from datetime import date, timedelta;
indata  = open('{{INFILE}}').read().strip()
input   = pickle.loads(base64.b64decode(indata));
output  = input+timedelta(days=1);
outdata = base64.b64encode(pickle.dumps(output)).decode();
print(outdata, file=open('{{OUTFILE}}','w'), end='')" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            infile_ext=".pkl.b64",
            outfile_ext=".pkl.b64",
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.pkl.b64",
            "task-io/outfile-{UUID}.pkl.b64",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


@pytest.mark.parametrize("quarantine", [None, 20])
async def test_400__exception_quarantine(
    queue_incoming: str,
    queue_outgoing: str,
    quarantine: Optional[int],
) -> None:
    """Test handling for exception w/ and w/o quarantine."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    # msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()

    # run producer & consumer concurrently
    error = ContainerRunError(
        1,
        "ValueError: no good!",
        os.environ["CI_TEST_ALPINE_PYTHON_IMAGE"],
    )
    with pytest.raises(
        RuntimeError, match=re.escape(f"1 TASK(S) FAILED: {repr(error)}")
    ):
        await asyncio.gather(
            populate_queue(
                queue_incoming,
                msgs_to_subproc,
                intermittent_sleep=TIMEOUT_INCOMING / 4,
            ),
            consume_and_reply(
                f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
                """python3 -c "raise ValueError('no good!')" """,
                queue_incoming=queue_incoming,
                queue_outgoing=queue_outgoing,
                timeout_incoming=TIMEOUT_INCOMING,
                quarantine_time=quarantine if quarantine else 0,
            ),
        )

    if quarantine:
        assert time.time() - start_time >= quarantine  # did quarantine_time work?
    else:
        assert time.time() - start_time <= 6  # no quarantine time # it's a magic number

    await assert_results(queue_outgoing, [])
    assert_pilot_dirs(
        1,  # only 1 message was processed before error
        [
            "task-io/infile-{UUID}.in",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


async def test_420__timeout(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test handling on a timeout."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    # msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()
    task_timeout = 2

    # run producer & consumer concurrently
    with pytest.raises(
        RuntimeError,
        match=re.escape(
            f"1 TASK(S) FAILED: TimeoutError('subprocess timed out after {task_timeout}s')"
        ),
    ):
        await asyncio.gather(
            populate_queue(
                queue_incoming,
                msgs_to_subproc,
                intermittent_sleep=TIMEOUT_INCOMING / 4,
            ),
            consume_and_reply(
                f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
                """python3 -c "import time; time.sleep(30)" """,
                queue_incoming=queue_incoming,
                queue_outgoing=queue_outgoing,
                timeout_incoming=TIMEOUT_INCOMING,
                task_timeout=task_timeout,
            ),
        )

    assert time.time() - start_time <= 5  # no quarantine time

    await assert_results(queue_outgoing, [])
    assert_pilot_dirs(
        1,
        [
            "task-io/infile-{UUID}.in",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


MAX_CONCURRENT_TASKS = 4
PREFETCH_TEST_PARAMETERS = sorted(
    set(
        [
            ENV.EWMS_PILOT_PREFETCH,
            1,
            2,
            MAX_CONCURRENT_TASKS - 1,
            MAX_CONCURRENT_TASKS,
            MAX_CONCURRENT_TASKS + 1,
            77,
        ]
    )
)


@pytest.mark.parametrize("prefetch", PREFETCH_TEST_PARAMETERS)
async def test_500__concurrent_load_max_concurrent_tasks(
    queue_incoming: str,
    queue_outgoing: str,
    prefetch: int,
) -> None:
    """Test max_concurrent_tasks within the pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import time
output = open('{{INFILE}}').read().strip() * 2;
time.sleep(5)
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
            prefetch=prefetch,
            max_concurrent_tasks=MAX_CONCURRENT_TASKS,
        ),
    )

    # it should've taken ~5 seconds to complete all tasks (but we're on 1 cpu so it takes longer)
    print(time.time() - start_time)

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


@pytest.mark.flaky(  # https://pypi.org/project/pytest-retry/
    # retry ONLY RABBITMQ -- run test on all
    retries=3,
    delay=1,
    condition=config.ENV.EWMS_PILOT_QUEUE_INCOMING_BROKER_TYPE == "rabbitmq",
)
@pytest.mark.parametrize("prefetch", PREFETCH_TEST_PARAMETERS)
async def test_510__concurrent_load_max_concurrent_tasks_exceptions(
    queue_incoming: str,
    queue_outgoing: str,
    prefetch: int,
) -> None:
    """Test max_concurrent_tasks within the pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()

    # run producer & consumer concurrently
    error = ContainerRunError(
        1,
        "ValueError: gotta fail!",
        os.environ["CI_TEST_ALPINE_PYTHON_IMAGE"],
    )
    with pytest.raises(
        RuntimeError,
        match=re.escape(f"{MAX_CONCURRENT_TASKS} TASK(S) FAILED: ")
        + ", ".join(re.escape(repr(error)) for _ in range(MAX_CONCURRENT_TASKS)),
    ) as e:
        await asyncio.gather(
            populate_queue(
                queue_incoming,
                msgs_to_subproc,
                # for some reason the delay has timing issues with rabbitmq & prefetch=1
                intermittent_sleep=(
                    TIMEOUT_INCOMING / 4
                    if not (
                        prefetch == 1
                        and config.ENV.EWMS_PILOT_QUEUE_INCOMING_BROKER_TYPE
                        == "rabbitmq"
                    )
                    else 0
                ),
            ),
            consume_and_reply(
                f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
                """python3 -c "
import time
output = open('{{INFILE}}').read().strip() * 2;
time.sleep(5)
print(output, file=open('{{OUTFILE}}','w'))
raise ValueError('gotta fail!')" """,  # double cat
                queue_incoming=queue_incoming,
                queue_outgoing=queue_outgoing,
                timeout_incoming=TIMEOUT_INCOMING,
                prefetch=prefetch,
                max_concurrent_tasks=MAX_CONCURRENT_TASKS,
            ),
        )
    # check each exception only occurred n-times -- much easier this way than regex (lots of permutations)
    # we already know there are MAX_CONCURRENT_TASKS subproc errors
    for msg in msgs_outgoing_expected:
        assert str(e.value).count(f"ValueError: gotta fail: {msg.strip()}") <= 1

    # it should've taken ~5 seconds to complete all tasks (but we're on 1 cpu so it takes longer)
    print(time.time() - start_time)

    await assert_results(queue_outgoing, [])
    assert_pilot_dirs(
        MAX_CONCURRENT_TASKS,
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


@pytest.mark.parametrize("prefetch", PREFETCH_TEST_PARAMETERS)
async def test_520__preload_max_concurrent_tasks(
    queue_incoming: str,
    queue_outgoing: str,
    prefetch: int,
) -> None:
    """Test max_concurrent_tasks within the pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()

    await populate_queue(
        queue_incoming,
        msgs_to_subproc,
        intermittent_sleep=TIMEOUT_INCOMING / 4,
    )

    await consume_and_reply(
        f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
        """python3 -c "
import time
output = open('{{INFILE}}').read().strip() * 2;
time.sleep(5)
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
        queue_incoming=queue_incoming,
        queue_outgoing=queue_outgoing,
        timeout_incoming=TIMEOUT_INCOMING,
        prefetch=prefetch,
        max_concurrent_tasks=MAX_CONCURRENT_TASKS,
    )

    # it should've taken ~5 seconds to complete all tasks (but we're on 1 cpu so it takes longer)
    print(time.time() - start_time)

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


@pytest.mark.parametrize("prefetch", PREFETCH_TEST_PARAMETERS)
async def test_530__preload_max_concurrent_tasks_exceptions(
    queue_incoming: str,
    queue_outgoing: str,
    prefetch: int,
) -> None:
    """Test max_concurrent_tasks within the pilot."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    start_time = time.time()

    await populate_queue(
        queue_incoming,
        msgs_to_subproc,
        intermittent_sleep=TIMEOUT_INCOMING / 4,
    )

    error = ContainerRunError(
        1,
        "ValueError: gotta fail!",
        os.environ["CI_TEST_ALPINE_PYTHON_IMAGE"],
    )
    with pytest.raises(
        RuntimeError,
        match=re.escape(f"{MAX_CONCURRENT_TASKS} TASK(S) FAILED: ")
        + ", ".join(re.escape(repr(error)) for _ in range(MAX_CONCURRENT_TASKS)),
    ) as e:
        await consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import time
output = open('{{INFILE}}').read().strip() * 2;
time.sleep(5)
print(output, file=open('{{OUTFILE}}','w'))
raise ValueError('gotta fail!')" """,  # double cat
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
            prefetch=prefetch,
            max_concurrent_tasks=MAX_CONCURRENT_TASKS,
        )
    # check each exception only occurred n-times -- much easier this way than regex (lots of permutations)
    # we already know there are MAX_CONCURRENT_TASKS subproc errors
    for msg in msgs_outgoing_expected:
        assert str(e.value).count(f"ValueError: gotta fail: {msg.strip()}") <= 1

    # it should've taken ~5 seconds to complete all tasks (but we're on 1 cpu so it takes longer)
    print(time.time() - start_time)

    await assert_results(queue_outgoing, [])
    assert_pilot_dirs(
        MAX_CONCURRENT_TASKS,
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


########################################################################################


async def _test_1000__heartbeat_workaround__rabbitmq_only(
    queue_incoming: str,
    queue_outgoing: str,
    refresh_interval_rabbitmq_heartbeat_interval: float,
) -> None:
    """Test just for rabbitmq.

    NOTE: CALLED IN TOP-MOST FUNCTION -- SEE SECTION'S BLOCK COMMENT THERE FOR WHY
    """
    msgs_to_subproc = MSGS_TO_SUBPROC[:2]
    # ^^^ should be sufficient plus avoids waiting for all to send
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    timeout_incoming = int(refresh_interval_rabbitmq_heartbeat_interval * 1.5)

    async def _test() -> None:
        await asyncio.gather(
            populate_queue(
                queue_incoming,
                msgs_to_subproc,
                intermittent_sleep=timeout_incoming / 4,
            ),
            consume_and_reply(
                f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
                """python3 -c "
import time;
output = open('{{INFILE}}').read().strip() * 2;
time.sleep("""
                + str(TEST_1000_SLEEP)
                + """);
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
                queue_incoming=queue_incoming,
                queue_outgoing=queue_outgoing,
                timeout_incoming=timeout_incoming,
            ),
        )

    # run producer & consumer concurrently
    with (
        patch(
            "ewms_pilot.pilot.REFRESH_INTERVAL",  # patch at 'ewms_pilot.pilot' bc using from-import
            refresh_interval_rabbitmq_heartbeat_interval,
        ),
        patch(
            "ewms_pilot.housekeeping.Housekeeping.RABBITMQ_HEARTBEAT_INTERVAL",
            refresh_interval_rabbitmq_heartbeat_interval,
        ),
    ):
        if refresh_interval_rabbitmq_heartbeat_interval > TEST_1000_SLEEP:
            with pytest.raises(
                RuntimeError,
                match=re.escape(
                    "1 TASK(S) FAILED: MQClientException('pika.exceptions.StreamLostError: may be due to a missed heartbeat')"
                ),
            ):
                await _test()
                await assert_results(queue_outgoing, [])
                assert_pilot_dirs(
                    len([]),
                    [
                        "task-io/infile-{UUID}.in",
                        "task-io/outfile-{UUID}.out",
                        "task-io/",
                        "outputs/stderrfile",
                        "outputs/stdoutfile",
                        "outputs/",
                    ],
                )
        elif refresh_interval_rabbitmq_heartbeat_interval == TEST_1000_SLEEP:
            with pytest.raises(mq.broker_client_interface.ClosingFailedException):
                await _test()
                await assert_results(queue_outgoing, [])
                assert_pilot_dirs(
                    len([]),
                    [
                        "task-io/infile-{UUID}.in",
                        "task-io/outfile-{UUID}.out",
                        "task-io/",
                        "outputs/stderrfile",
                        "outputs/stdoutfile",
                        "outputs/",
                    ],
                )
        else:  # refresh_interval_rabbitmq_heartbeat_interval < TEST_1000_SLEEP
            await _test()
            await assert_results(queue_outgoing, msgs_outgoing_expected)
            assert_pilot_dirs(
                len(msgs_outgoing_expected),
                [
                    "task-io/infile-{UUID}.in",
                    "task-io/outfile-{UUID}.out",
                    "task-io/",
                    "outputs/stderrfile",
                    "outputs/stdoutfile",
                    "outputs/",
                ],
            )


########################################################################################


async def test_2000_init(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal init command."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
output = open('{{INFILE}}').read().strip() * 2;
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
import os
with open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput', 'w') as f:
    print('writing hello world to a file...')
    print('hello world!', file=f)
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "hello world!"

    # check task stuff
    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
        ["initoutput"],
        has_init_cmd_subdir=True,
    )


async def test_2001_init__timeout_error(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a init command with error."""
    init_timeout = 10  # something long enough to account for docker time

    with pytest.raises(
        TimeoutError,
        match=re.escape(f"subprocess timed out after {init_timeout}s"),
    ):
        await consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
output = open('{{INFILE}}').read().strip() * 2;
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args=f"""python3 -c "
import time
import os
with open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput', 'w') as f:
    print('writing hello world to a file...')
    print('hello world!', file=f)
time.sleep({init_timeout})
" """,
            init_timeout=init_timeout,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "hello world!"


async def test_2002_init__exception(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a init command with error."""

    with pytest.raises(
        ContainerRunError,
        match=re.escape(
            str(  # -> only the message part
                ContainerRunError(
                    1,
                    "ValueError: no good!",
                    os.environ["CI_TEST_ALPINE_PYTHON_IMAGE"],
                )
            )
        ),
    ):
        await consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
output = open('{{INFILE}}').read().strip() * 2;
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
import os
with open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput', 'w') as f:
    print('writing hello world to a file...')
    print('hello world!', file=f)
raise ValueError('no good!')
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "hello world!"


async def test_2100_use_data_hub_in_init_and_tasks__env_var(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal init container's data hub file in another task."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}blue\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import os
output = open('{{INFILE}}').read().strip() + open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput').read().strip();
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
import os
with open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput', 'w') as f:
    print('writing to a file...')
    print('blue', file=f)
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "blue"

    # check task stuff
    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
        ["initoutput"],
        has_init_cmd_subdir=True,
    )


async def test_2110_use_data_hub_in_init_and_tasks__arg_placeholder(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a normal init container's data hub file in another task."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}blue\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
output = open('{{INFILE}}').read().strip() + open('{{DATA_HUB}}' + '/initoutput').read().strip();
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
with open('{{DATA_HUB}}' + '/initoutput', 'w') as f:
    print('writing to a file...')
    print('blue', file=f)
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "blue"

    # check task stuff
    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
        ["initoutput"],
        has_init_cmd_subdir=True,
    )


########################################################################################


async def test_3000_external_directories(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test accessing user-supplied external directories."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}alphabeta\n" for x in msgs_to_subproc]

    assert os.getenv("EWMS_PILOT_EXTERNAL_DIRECTORIES")

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import os
file_one='/cvmfs/dummy-1/dir-A/file.txt'
file_two='/cvmfs/dummy-2/dir-B/file.txt'
output = open('{{INFILE}}').read().strip() + open(file_one).read().strip() + open(file_two).read().strip();
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
file_one='/cvmfs/dummy-1/dir-A/file.txt'
assert open(file_one).read().strip() == 'alpha'
file_two='/cvmfs/dummy-2/dir-B/file.txt'
assert open(file_two).read().strip() == 'beta'
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    # check task stuff
    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
        [],
        has_init_cmd_subdir=True,
    )


########################################################################################


async def test_4000__no_output_ok(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a pilot with no outfile."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    # msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            "sleep .1",
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, [])
    assert_pilot_dirs(
        len(msgs_to_subproc),
        [
            "task-io/infile-{UUID}.in",
            # "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )


########################################################################################


async def test_5000__io_from_envvars(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a pilot that gets io filepaths from env vars."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import os
output = open(os.environ['EWMS_TASK_INFILE']).read().strip() * 2;
print(output, file=open(os.environ['EWMS_TASK_OUTFILE'],'w'))" """,  # double cat
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
    )

    ########################################################################################


async def test_6000__task_env_vars(
    queue_incoming: str,
    queue_outgoing: str,
) -> None:
    """Test a pilot that reads env vars that are defined for the task by the user."""
    msgs_to_subproc = MSGS_TO_SUBPROC
    msgs_outgoing_expected = [f"{x}{x}\n" for x in msgs_to_subproc]

    # set the env vars -- this will work fine as long as there is no immediate processing in package (like dataclass's __post_init__)
    # use object.__setattr__ b/c dataclass is frozen
    object.__setattr__(
        ENV, "EWMS_PILOT_INIT_ENV_JSON", json.dumps({"INIT_FOO": "BOT", "INIT_BAZ": 99})
    )
    object.__setattr__(
        ENV, "EWMS_PILOT_TASK_ENV_JSON", json.dumps({"FOO": "BAR", "BAZ": 100})
    )

    # run producer & consumer concurrently
    await asyncio.gather(
        populate_queue(
            queue_incoming,
            msgs_to_subproc,
            intermittent_sleep=TIMEOUT_INCOMING / 4,
        ),
        consume_and_reply(
            f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            """python3 -c "
import os
output = open('{{INFILE}}').read().strip() * 2;
assert os.environ['FOO'] == 'BAR'
assert os.environ['BAZ'] == '100'
print(output, file=open('{{OUTFILE}}','w'))" """,  # double cat
            #
            init_image=f"{os.environ['CI_TEST_ALPINE_PYTHON_IMAGE']}",
            init_args="""python3 -c "
import os
assert os.environ['INIT_FOO'] == 'BOT'
assert os.environ['INIT_BAZ'] == '99'
with open(os.environ['EWMS_TASK_DATA_HUB_DIR'] + '/initoutput', 'w') as f:
    print('writing hello world to a file...')
    print('hello world!', file=f)
" """,
            queue_incoming=queue_incoming,
            queue_outgoing=queue_outgoing,
            timeout_incoming=TIMEOUT_INCOMING,
        ),
    )

    # check init's output
    with open(PILOT_DATA_DIR / PILOT_DATA_HUB_DIR_NAME / "initoutput") as f:
        assert f.read().strip() == "hello world!"

    # check task stuff
    await assert_results(queue_outgoing, msgs_outgoing_expected)
    assert_pilot_dirs(
        len(msgs_outgoing_expected),
        [
            "task-io/infile-{UUID}.in",
            "task-io/outfile-{UUID}.out",
            "task-io/",
            "outputs/stderrfile",
            "outputs/stdoutfile",
            "outputs/",
        ],
        ["initoutput"],
        has_init_cmd_subdir=True,
    )
