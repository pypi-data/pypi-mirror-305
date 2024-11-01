import abc
from typing import Protocol


class ClickhouseSettingsProtocol(Protocol):
    """
    see: https://clickhouse.com/docs/en/operations/settings/settings
    """
    @abc.abstractmethod
    def set_settings(self, settings: dict):
        pass

    @property
    def settings(self) -> dict:
        pass

    @abc.abstractmethod
    def skip_settings(self):
        pass
