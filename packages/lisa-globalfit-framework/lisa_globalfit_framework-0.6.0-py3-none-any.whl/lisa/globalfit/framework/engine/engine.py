import asyncio
import logging
from asyncio import Event, Future
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

from lisa.globalfit.framework.bus import EventBus
from lisa.globalfit.framework.engine.rule import Response, Rule
from lisa.globalfit.framework.msg.subjects import Subject

logger = logging.getLogger(__name__)


class Engine:
    def __init__(self, bus: EventBus, rules: list[Rule]) -> None:
        self.bus = bus
        self.rules = rules
        self.handlers: dict[Subject, list[Rule]] = defaultdict(list)
        self.wake = Event()
        self.should_stop = Event()
        self.executor = ProcessPoolExecutor()
        self.running_tasks: set[Future] = set()

    async def setup(self) -> None:
        await self.bus.connect()
        await self.register_rules()

    async def register_rules(self) -> None:
        await asyncio.gather(*(self.register_rule(r) for r in self.rules))

    async def register_rule(self, rule: Rule) -> None:
        await self.bus.subscribe(rule.subject, self.handle_message)
        self.handlers[rule.subject].append(rule)
        logger.info(f"loaded rule {rule.id!r}")

    async def run(self) -> None:
        logger.info("starting rule engine")
        while not self.should_stop.is_set():
            if not self.running_tasks:
                logger.info("waiting for next event")
                # Relying on a wake event is necessary because we can't wait on an
                # empty list of coroutines.
                await self.wake.wait()

            self.wake.clear()
            logger.info(f"waiting for {len(self.running_tasks)} pending tasks")
            done, _ = await asyncio.wait(
                self.running_tasks, return_when=asyncio.FIRST_COMPLETED
            )
            self.running_tasks -= done
            await asyncio.gather(*(self.handle_result(result) for result in done))

        await self.shutdown()

    async def handle_result(self, task: Future) -> None:
        error = task.exception()
        if error is not None:
            logger.error(f"got exception for task {task}: {error}")
            return

        responses: list[Response] = task.result()
        await asyncio.gather(
            *(
                self.bus.publish(response.subject, response.msg.encode())
                for response in responses
            )
        )

    async def handle_message(self, subject: Subject, msg: bytes) -> None:
        handlers = self.handlers.get(subject)
        if handlers is None:
            logger.warning(f"no handlers for message on subject {subject!r}")
            return

        await asyncio.gather(
            *(self.run_handler(handler, subject, msg) for handler in handlers)
        )

    async def run_handler(self, rule: Rule, subject: Subject, msg: bytes) -> None:
        if not rule.is_active:
            logger.info(f"skipping evaluation of inactive rule {rule.id!r}")
            return

        logger.info(f"scheduling evaluation of rule {rule.id!r}")
        loop = asyncio.get_event_loop()
        task = loop.run_in_executor(self.executor, rule.evaluate, subject, msg)
        self.running_tasks.add(task)
        self.wake.set()

    async def publish_responses(self, responses: list[Response]) -> None:
        await asyncio.gather(
            *(self.bus.publish(r.subject, r.msg.encode()) for r in responses)
        )

    async def shutdown(self) -> None:
        logger.info("shutting down engine")
        await self.bus.close()
        self.executor.shutdown()
