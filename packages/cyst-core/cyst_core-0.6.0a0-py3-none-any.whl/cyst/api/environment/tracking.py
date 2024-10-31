from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto

from cyst.api.host.service import Service
from cyst.api.network.elements import Connection, Port, Interface, Route
from cyst.api.network.node import Node
from cyst.api.network.session import Session


class Mode(Enum):
    ADD = auto()
    MODIFY = auto()
    REMOVE = auto()


class EnvironmentTracking(ABC):

    @abstractmethod
    def track(self, mode: Mode, item: Node | Service | Session):
        pass
