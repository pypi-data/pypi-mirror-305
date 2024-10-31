import abc
from typing import Protocol


class ClickhouseOnClusterProtocol(Protocol):
    @abc.abstractmethod
    def set_on_cluster(self, name: str):
        pass

    @property
    def on_cluster(self) -> str:
        pass

    @abc.abstractmethod
    def skip_on_cluster(self):
        pass
