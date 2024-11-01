import abc
from typing import Protocol

from .._protocols.clickhouse_db import ClickhouseDbProtocol
from .._protocols.clickhouse_partition import ClickhousePartitionProtocol
from .._protocols.clickhouse_system import ClickhouseSystemProtocol
from .._protocols.clickhouse_table import ClickhouseTableProtocol


class ClickhouseProtocol(Protocol, metaclass=abc.ABCMeta):
    @property
    def active_db(self) -> str:
        pass

    @abc.abstractmethod
    def ping(self) -> bool:
        pass

    @abc.abstractmethod
    def get_table_protocol(self) -> ClickhouseTableProtocol:
        pass

    @abc.abstractmethod
    def get_system_protocol(self) -> ClickhouseSystemProtocol:
        pass

    @abc.abstractmethod
    def get_partition_protocol(self) -> ClickhousePartitionProtocol:
        pass

    @abc.abstractmethod
    def get_db_protocol(self) -> ClickhouseDbProtocol:
        pass
