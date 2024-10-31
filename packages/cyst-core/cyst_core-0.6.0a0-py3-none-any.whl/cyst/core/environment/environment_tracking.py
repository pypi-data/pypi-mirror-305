from cyst.api.environment.infrastructure import DataStore
from cyst.api.environment.tracking import EnvironmentTracking, Mode
from cyst.api.host.service import Service
from cyst.api.network.node import Node
from cyst.api.network.session import Session


class EnvironmentTrackingImpl(EnvironmentTracking):

    def __init__(self, run_id: str, data_store: DataStore, enabled: bool = True, use_console: bool = True,
                 use_data_store: bool = False):
        self._run_id = run_id
        self._data_store = data_store

        self._enabled = enabled
        self._use_console = use_console
        self._use_data_store = use_data_store

    def track(self, mode: Mode, item: Node | Service | Session):
        if not self._enabled:
            return

        if mode == Mode.ADD:
            self._track_add(item)
        elif mode == Mode.MODIFY:
            self._track_modify(item)
        else:
            self._track_remove(item)

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def _track_add(self, item: Node | Service | Session):
        print(f"New item added to state: {item}")

    def _track_modify(self, item):
        pass

    def _track_remove(self, item):
        pass