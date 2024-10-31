from typing import Any

from .cmd_service import CmdService
from .system_service import SystemService
from .._protocols.clickhouse_table import ClickhouseTableProtocol
from .._sql_cmd.clickhouse import (
    RenameTableOnCluster,
    TruncateOnClusterCmd,
    CreateTableAsOnClusterCmd,
    InsertFromS3Cmd,
    InsertIntoS3Cmd,
    ClickhouseS3SettingsModel,
)
from ..clickhouse_models.table import ClickhouseTableModel


class TableService(CmdService, ClickhouseTableProtocol):
    def __init__(self, client: Any, system_service: SystemService) -> None:
        super().__init__(client)
        self._system_service = system_service

    def create_table_as(
        self,
        from_table: ClickhouseTableModel,
        table: str,
        db: str = '',
        order_by: list = None,
        partition_by: list = None,
        engine: str = ''
    ) -> ClickhouseTableModel:
        table_full_name = self.get_full_table_name(table, db)
        order = f'ORDER BY {", ".join(order_by) if order_by else from_table.sorting_key}'
        partition = ", ".join(partition_by) if partition_by else from_table.partition_key
        if partition:
            partition = f'PARTITION BY {partition}'

        self._run_cmd(
            CreateTableAsOnClusterCmd,
            model_params=dict(
                table_name=table_full_name,
                from_table=from_table.full_name,
                order_by=order,
                partition_by=partition,
                engine=engine if engine else from_table.engine,
            ),
        )

        return self._system_service.get_table_by_name(table, db)

    def insert_from_table(self, from_table: ClickhouseTableModel, to_table: ClickhouseTableModel) -> None:
        self._client.execute(f"""
            INSERT INTO {to_table.full_name}
            SELECT * FROM {from_table.full_name}
        """)

    def truncate(self, table: str, db: str = '') -> None:
        on_cluster = self.on_cluster
        table_name = self.get_full_table_name(table, db)
        self._run_cmd(
            TruncateOnClusterCmd,
            model_params=dict(table_name=table_name, on_cluster=on_cluster),
        )

    def insert_from_s3(self, table: ClickhouseTableModel, s3_settings: ClickhouseS3SettingsModel):
        self._run_cmd(
            InsertFromS3Cmd,
            model_params=dict(table_name=table.full_name, s3_settings=s3_settings),
        )

    def insert_table_to_s3(self, table: ClickhouseTableModel, s3_settings: ClickhouseS3SettingsModel):
        self._run_cmd(
            InsertIntoS3Cmd,
            model_params=dict(table_name=table.full_name, s3_settings=s3_settings),
        )

    def rename_table(self, table: ClickhouseTableModel, new_name: str, db: str = '') -> ClickhouseTableModel:
        on_cluster = self.on_cluster
        full_name = self.get_full_table_name(new_name, db)
        self._run_cmd(
            RenameTableOnCluster,
            model_params=dict(table=table.full_name, new_name=full_name, on_cluster=on_cluster),
        )

        return self._system_service.get_table_by_name(new_name, db)
