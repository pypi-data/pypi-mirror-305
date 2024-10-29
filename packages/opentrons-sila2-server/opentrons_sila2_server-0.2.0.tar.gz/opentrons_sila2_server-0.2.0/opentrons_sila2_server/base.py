import uuid
from threading import Lock
from typing import Dict

from opentrons.protocol_api import ProtocolContext

from .labware.labware_wrapper import LabwareWrapper

class Base:
    def __init__(self):
        self._lock = Lock()
        self.session_id: str | None = None
        self.protocol: ProtocolContext | None = None
        self.labwares: Dict[str, LabwareWrapper] = {}

    """Session"""

    def start_session(self) -> str | None:
        self._lock.acquire(blocking=True)
        if self.session_id is None:
            self.session_id = str(uuid.uuid4())
            self._lock.release()
            return self.session_id
        else:
            self._lock.release()
            return None

    def end_session(self, session_id: str) -> None:
        self._lock.acquire(blocking=True)
        if self.session_id == session_id:
            self.protocol.cleanup()
            self.session_id = None
        self._lock.release()

    def get_session_id(self) -> str | None:
        self._lock.acquire(blocking=True)
        if not self.session_id:
            self._lock.release()
            return None
        new_session_id = str(self.session_id)
        self._lock.release()
        return new_session_id

    def set_session_protocol(self, protocol: ProtocolContext) -> None:
        self._lock.acquire(blocking=True)
        self.protocol = protocol
        self._lock.release()

    """Labware"""

    def add_labware(self, labware: LabwareWrapper, identifier: str):
        self._lock.acquire(blocking=True)
        self.labwares[identifier] = labware
        self._lock.release()

    def get_labware(self, identifier: str) -> LabwareWrapper:
        return self.labwares[identifier]

    def get_labware_by_position(self, position: str) -> LabwareWrapper | None:
        for labware in self.labwares.values():
            if(labware.position == position):
                return labware
        return None

    def delete_labware(self, identifier: str):
        self._lock.acquire(blocking=True)
        self.labwares.pop(identifier)
        self._lock.release()
