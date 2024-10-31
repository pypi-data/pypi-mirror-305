import asyncio
import json
import logging
import subprocess
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass, field

from lisa.globalfit.framework.args import add_bus_args, add_common_args
from lisa.globalfit.framework.buses.nats import NatsEventBus
from lisa.globalfit.framework.engine.rule import Response, Rule
from lisa.globalfit.framework.msg.base import MessageBase

logger = logging.getLogger(__name__)

INBOX = "infra.pipelinerunner.submit"
OUTBOX = "infra.pipelinerunner.result"


@dataclass
class WorkflowSpec(MessageBase):
    resource: str
    labels: list[str] = field(default_factory=list)


@dataclass
class WorkflowResult(MessageBase):
    status: str
    labels: list[str] = field(default_factory=list)


class SubmitWorkflow(Rule):
    def evaluate(self, subject: str, msg: bytes) -> list[Response]:
        if subject != INBOX:
            logger.warning(f"got workflow submission from unexpected subject {subject}")
            return []

        spec = WorkflowSpec.decode(msg)
        result = self.submit_workflow(spec)

        return [Response(OUTBOX, result)]

    def submit_workflow(self, spec: WorkflowSpec) -> WorkflowResult:
        logger.info(f"submitting workflow {spec}")
        proc = subprocess.run(
            ["argo", "submit", "--output", "name", "--wait", spec.resource],
            capture_output=True,
        )
        if proc.returncode != 0:
            raise ValueError(
                f"could not submit workflow: {proc.stderr.decode().strip()}"
            )

        workflow_name = proc.stdout.decode().strip()

        return self.get_workflow_status(spec, workflow_name)

    def get_workflow_status(self, spec: WorkflowSpec, name: str) -> WorkflowResult:
        logger.info(f"fetching status of workflow {name!r}")
        proc = subprocess.run(
            ["argo", "get", "--output", "json", name],
            capture_output=True,
        )
        if proc.returncode != 0:
            raise ValueError(
                f"could not get workflow status: {proc.stderr.decode().strip()}"
            )

        contents = json.loads(proc.stdout)
        return WorkflowResult(contents["status"]["phase"], spec.labels)


__rule__ = SubmitWorkflow(id="pipelinerunner-bridge", is_active=True, subject=INBOX)


def get_args() -> Namespace:
    parser = ArgumentParser()

    add_common_args(parser)
    add_bus_args(parser)

    parser.add_argument(
        "workflow",
        type=str,
    )

    parser.add_argument(
        "--labels",
        type=str,
        nargs="+",
    )

    return parser.parse_args()


async def main_async():
    args = get_args()
    logging.basicConfig(
        level=args.log_level,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s %(message)s",
        datefmt=r"%Y-%m-%dT%H:%M:%S",
    )
    bus = NatsEventBus(servers=args.servers)
    spec = WorkflowSpec(
        resource=args.workflow, labels=args.labels if args.labels is not None else []
    )
    await bus.connect()
    await bus.publish(INBOX, spec.encode())
    logger.info(f"submitted workflow {spec}")


def main():
    return asyncio.run(main_async())


if __name__ == "__main__":
    main()
