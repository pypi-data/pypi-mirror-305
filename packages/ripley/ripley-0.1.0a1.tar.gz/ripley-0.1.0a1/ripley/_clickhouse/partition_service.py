from typing import Any

from .cmd_service import CmdService
from .system_service import SystemService
from .._protocols.clickhouse_partition import ClickhousePartitionProtocol
from .._sql_cmd.clickhouse import (
    DetachPartitionOnClusterCmd,
    AttachPartitionOnClusterCmd,
    DropPartitionOnClusterCmd,
    MovePartitionOnClusterCmd,
    ReplacePartitionOnClusterCmd,
)
from ..clickhouse_models.table import ClickhouseTableModel as CTable


class PartitionService(CmdService, ClickhousePartitionProtocol):
    def __init__(self, client: Any, system_service: SystemService) -> None:
        super().__init__(client)
        self._system_service = system_service

    def move_partition(self, from_table: CTable, to_table: CTable, partition: str) -> None:
        on_cluster = self.on_cluster
        self._run_cmd(
            MovePartitionOnClusterCmd,
            model_params=dict(
                to_table_name=to_table.full_name,
                table_name=from_table.full_name,
                partition=partition,
                on_cluster=on_cluster,
            ),
        )

    def drop_partition(self, table: CTable, partition: str) -> None:
        on_cluster = self.on_cluster
        self._run_cmd(
            DropPartitionOnClusterCmd,
            model_params=dict(
                table_name=table.full_name,
                partition=partition,
                on_cluster=on_cluster,
            ),
        )

    def replace_partition(self, from_table: CTable, to_table: CTable, partition: str) -> None:
        on_cluster = self.on_cluster
        self._run_cmd(
            ReplacePartitionOnClusterCmd,
            model_params=dict(
                table_name=to_table.full_name,
                partition=partition,
                from_table_name=from_table.full_name,
                on_cluster=on_cluster,
            ),
        )

    def detach_partition(self, table: CTable, partition: str) -> None:
        on_cluster = self.on_cluster
        self._run_cmd(
            DetachPartitionOnClusterCmd,
            model_params=dict(
                table_name=table.full_name,
                partition=partition,
                on_cluster=on_cluster,
            ),
        )

    def attach_partition(self, table: CTable, partition: str) -> None:
        on_cluster = self.on_cluster
        self._run_cmd(
            AttachPartitionOnClusterCmd,
            model_params=dict(
                table_name=table.full_name,
                partition=partition,
                on_cluster=on_cluster,
            ),
        )
