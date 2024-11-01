from typing import Any

from .cmd_service import CmdService
from .system_service import SystemService
from .._protocols.clickhouse_db import ClickhouseDbProtocol
from .._sql_cmd.clickhouse import CreateDbOnCluster
from ..clickhouse_models.db import ClickhouseDbModel


class DbService(CmdService, ClickhouseDbProtocol):
    def __init__(self, client: Any, system_service: SystemService) -> None:
        super().__init__(client)
        self._system_service = system_service

    def create_db(self, name: str, on_cluster: str = '', engine: str = '') -> ClickhouseDbModel:
        on_cluster = self.on_cluster
        self._run_cmd(
            CreateDbOnCluster,
            model_params=dict(name=name, on_cluster=on_cluster, engine=engine),
        )

        return self._system_service.get_database_by_name(name)
