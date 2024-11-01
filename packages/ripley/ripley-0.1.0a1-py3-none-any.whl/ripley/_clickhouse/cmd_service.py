import re
from copy import deepcopy
from typing import Any, Type, List, Dict

from .._log import log
from .._protocols.clickhouse_settings import ClickhouseSettingsProtocol
from .._protocols.clickhouse_on_cluster import ClickhouseOnClusterProtocol
from .._sql_cmd.clickhouse import AlterOnClusterCmd, CreateTableOnClusterCmd, TruncateOnClusterCmd, CreateDbOnCluster
from .._sql_cmd.general import AbstractSql


class CmdService(ClickhouseSettingsProtocol, ClickhouseOnClusterProtocol):
    def __init__(self, client: Any) -> None:
        self._client = client
        self._settings = {}
        self._on_cluster = ''

    @property
    def settings(self) -> dict:
        return self._settings

    @property
    def active_db(self) -> str:
        return self._client.get_connection().database

    @property
    def on_cluster(self) -> str:
        return self._on_cluster

    def get_full_table_name(self, table: str, db: str = '') -> str:
        return f'{db}.{table}' if db else f'{self.active_db}.{table}'

    def skip_on_cluster(self):
        self._on_cluster = ''

    def set_on_cluster(self, name: str):
        self._on_cluster = name

    def set_settings(self, settings: dict):
        self._settings = settings

    def skip_settings(self):
        self._settings = {}

    def _exec(self, sql: str, params: dict = None, with_column_types: bool = False):
        return self._client.execute(sql, params=params, with_column_types=with_column_types, settings=self._settings)

    def _get_records(self, sql: str, model: Type = None, params: dict = None) -> List[Any]:
        data, columns = self._exec(sql, params, True)
        columns = [re.sub(r'\W', '_', name) for name, type_ in columns]
        records = []

        for rec in data:
            params = {columns[ix_]: value_ for ix_, value_ in enumerate(rec)}
            records.append(model(**params) if model else params)

        return records

    def _get_first_record(self, sql: str, model: Type = None, params: dict = None) -> Any:
        records = self._get_records(sql, model, params)
        if records:
            return records[0]

    def _run_cmd(self, model_class: Type[AbstractSql], model_params: Dict) -> Any:
        params = deepcopy(model_params)
        if issubclass(
            model_class,
            (AlterOnClusterCmd, CreateTableOnClusterCmd, TruncateOnClusterCmd, CreateDbOnCluster)
        ):
            if self._on_cluster:
                params['on_cluster'] = self._on_cluster

        cmd = model_class(**params)
        log.info('%s\nSETTINGS %s', cmd, self._settings)
        self._exec(cmd.to_sql())
