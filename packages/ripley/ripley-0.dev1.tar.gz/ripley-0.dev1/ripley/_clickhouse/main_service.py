from typing import Any

from .cmd_service import CmdService
from .db_service import DbService
from .partition_service import PartitionService
from .system_service import SystemService
from .table_service import TableService
from .._protocols.clickhouse import ClickhouseProtocol
from .._protocols.clickhouse_db import ClickhouseDbProtocol
from .._protocols.clickhouse_table import ClickhouseTableProtocol
from .._protocols.clickhouse_partition import ClickhousePartitionProtocol
from .._protocols.clickhouse_system import ClickhouseSystemProtocol


class MainService(CmdService, ClickhouseProtocol):
    def __init__(self, client: Any) -> None:
        super().__init__(client)
        self._system_service = SystemService(client)
        self._partition_service = PartitionService(client, self._system_service)
        self._table_service = TableService(client, self._system_service)
        self._db_service = DbService(client, self._system_service)

    def ping(self) -> bool:
        return self._client.get_connection().ping()

    def get_table_protocol(self) -> ClickhouseTableProtocol:
        return self._table_service

    def get_system_protocol(self) -> ClickhouseSystemProtocol:
        return self._system_service

    def get_partition_protocol(self) -> ClickhousePartitionProtocol:
        return self._partition_service

    def get_db_protocol(self) -> ClickhouseDbProtocol:
        return self._db_service
