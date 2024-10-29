from random import random
from typing import (
    Awaitable,
    Callable,
    Coroutine,
    Optional,
    Union,
    TypeVar,
    runtime_checkable,
    Protocol,
    Any,
    Dict,
    List,
    AsyncIterator,
)
from rekuest_next.messages import Assign, OutMessage, Cancel
import uuid
from pydantic import Field
from rekuest_next.messages import AssignationEvent, ProvisionEvent
from rekuest_next.structures.default import get_default_structure_registry
from koil.composition import KoiledModel
from koil.types import ContextBool
import uuid
import asyncio
import logging
from rekuest_next.structures.registry import StructureRegistry
from rekuest_next.api.schema import (
    AssignationEventKind,
    BindsInput,
    Definition,
    HookInput,
    Reservation,
    Template,
    afind,
)
from .errors import (
    AssignException,
    IncorrectReserveState,
    PostmanException,
    RecoverableAssignException,
)
from rekuest_next.actors.base import Actor, SerializingActor
from rekuest_next.agents.transport.base import AgentTransport
from .base import BasePostman
from rekuest_next.actors.types import (
    Passport,
)
from enum import Enum

logger = logging.getLogger(__name__)

T = TypeVar("T")


class localuse(KoiledModel):
    template: Template
    supervisor: Actor
    constants: Optional[dict[str, Any]] = None
    reference: Optional[str] = None
    hooks: Optional[List[HookInput]] = None
    cached: bool = False
    parent: Optional[str] = None
    log: bool = False
    assignation_id: Optional[str] = None

    _managed_actor: Optional[Actor] = None
    _assign_queues: Optional[Dict[str, asyncio.Queue[OutMessage]]] = None

    async def __aenter__(self) -> "localuse":
        self._assign_queues = {}
        self._enter_future = asyncio.Future()
        self._updates_queue = asyncio.Queue[AssignationEvent]()

        self._managed_actor = await self.supervisor.aspawn_actor(
            self.template,
            on_log_event=self.on_actor_event,
        )

        await self._managed_actor.arun()
        await self._enter_future

    async def on_actor_event(self, message: OutMessage):
        if isinstance(message, ProvisionEvent):
            print("Actor entered")
            if self._enter_future and not self._enter_future.done():
                self._enter_future.set_result(None)
                return

        if message.id in self._assign_queues:
            await self._assign_queues[message.id].put(message)
        else:
            logger.error(f"Unexpected message: {message}")

    async def acall_raw(
        self,
        kwargs: Dict[str, Any],
        parent: Optional[Assign] = None,
        reference: str = None,
        assign_timeout: Optional[float] = None,
        timeout_is_recoverable: bool = False,
    ):

        assignment = Assign(
            assignation=parent.assignation if parent else None,
            parent=parent.assignation if parent else None,
            mother=parent.mother if parent else None,
            args=kwargs,
            user=parent.user if parent else None,
            reference=reference,
        )

        _ass_queue = asyncio.Queue[OutMessage]()
        self._assign_queues[assignment.id] = _ass_queue

        await self._managed_actor.apass(assignment)
        try:
            while True:  # Waiting for assignation
                logger.info("Waiting for update")
                ass = await asyncio.wait_for(
                    _ass_queue.get(), timeout=assign_timeout
                )
                logger.info(f"Local Assign Context: {ass}")
                if ass.kind == AssignationEventKind.YIELD:
                    return ass.returns

                if ass.kind in [AssignationEventKind.ERROR]:
                    raise RecoverableAssignException(
                        f"Recoverable Exception: {ass.message}"
                    )

                if ass.kind in [AssignationEventKind.CRITICAL]:
                    raise AssignException(f"Critical error: {ass.message}")

                if ass.status in [AssignationEventKind.CANCELLED]:
                    raise AssignException("Was cancelled from the outside")

                _ass_queue.task_done()
        except asyncio.CancelledError as e:
            await self._managed_actor.apass(
                Cancel(assignation=id, provision=self.supervisor.passport.provision)
            )

            ass = await asyncio.wait_for(_ass_queue.get(), timeout=2)
            if ass.kind == AssignationEventKind.CANCELLED:
                logger.info("Wonderfully cancelled that assignation!")
                raise e

            raise AssignException(f"Critical error: {ass}")

        except asyncio.TimeoutError as e:
            exc_class = (
                RecoverableAssignException
                if timeout_is_recoverable
                else AssignException
            )

            raise exc_class("Timeout error for assignation") from e

        except Exception as e:
            logger.error("Error in Assignation", exc_info=True)
            raise e

    async def aiterate(self, *args, **kwargs):
        raise NotImplementedError("Not implemented call raw instead")

    async def aiterate_raw(
        self,
        kwargs: Dict[str, Any],
        parent: Optional[Assign] = None,
        reference: str = None,
        assign_timeout: Optional[float] = None,
        timeout_is_recoverable: bool = False,
    ):
        print("Starting to iterate?")
        assignment = Assign(
            assignation=parent.assignation if parent else None,
            parent=parent.assignation if parent else None,
            mother=parent.mother if parent else None,
            args=kwargs,
            user=parent.user if parent else None,
            reference=reference,
        )

        _ass_queue = asyncio.Queue[OutMessage]()
        self._assign_queues[assignment.id] = _ass_queue

        await self._managed_actor.apass(assignment)
        try:
            while True:  # Waiting for assignation
                logger.info("Waiting for update")
                ass = await asyncio.wait_for(
                    _ass_queue.get(), timeout=assign_timeout
                )
                logger.info(f"Local Assign Context: {ass}")
                if ass.kind == AssignationEventKind.YIELD:
                    yield ass.returns

                if ass.kind == AssignationEventKind.DONE:
                    return

                if ass.kind in [AssignationEventKind.ERROR]:
                    raise RecoverableAssignException(
                        f"Recoverable Exception: {ass.message}"
                    )

                if ass.kind in [AssignationEventKind.CRITICAL]:
                    raise AssignException(f"Critical error: {ass.message}")

                if ass.status in [AssignationEventKind.CANCELLED]:
                    raise AssignException("Was cancelled from the outside")

                _ass_queue.task_done()
        except asyncio.CancelledError as e:
            await self._managed_actor.apass(
                Cancel(assignation=id, provision=self.supervisor.passport.provision)
            )

            ass = await asyncio.wait_for(_ass_queue.get(), timeout=2)
            if ass.kind == AssignationEventKind.CANCELLED:
                logger.info("Wonderfully cancelled that assignation!")
                raise e

            raise AssignException(f"Critical error: {ass}")

        except asyncio.TimeoutError as e:
            exc_class = (
                RecoverableAssignException
                if timeout_is_recoverable
                else AssignException
            )

            raise exc_class("Timeout error for assignation") from e

        except Exception as e:
            logger.error("Error in Assignation", exc_info=True)
            raise e

    async def aexit(self):
        if self._managed_actor:
            await self._managed_actor.acancel()
