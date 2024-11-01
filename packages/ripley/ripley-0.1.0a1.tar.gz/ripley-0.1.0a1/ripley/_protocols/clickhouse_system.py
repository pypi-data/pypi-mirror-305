import abc
from typing import Protocol, List

from ..clickhouse_models.db import ClickhouseDbModel
from ..clickhouse_models.disk import ClickhouseDiskModel
from ..clickhouse_models.partition import ClickhousePartitionModel
from ..clickhouse_models.process import ClickhouseProcessModel
from ..clickhouse_models.table import ClickhouseTableModel
from ..clickhouse_models.column import ClickhouseColumnModel


class ClickhouseSystemProtocol(Protocol, metaclass=abc.ABCMeta):
    """
    Provides information from system tables
    see: https://clickhouse.com/docs/en/operations/system-tables
    """
    @abc.abstractmethod
    def get_databases(self) -> List[ClickhouseDbModel]:
        """
        system.databases
        see: https://clickhouse.com/docs/en/operations/system-tables/databases
        """

    @abc.abstractmethod
    def get_database_by_name(self, name: str = '') -> 'ClickhouseDbModel':
        """
        system.databases
        see: https://clickhouse.com/docs/en/operations/system-tables/databases
        """

    @abc.abstractmethod
    def get_tables_by_db(self, db: str = '') -> List[ClickhouseTableModel]:
        """
        system.tables
        see: https://clickhouse.com/docs/en/operations/system-tables/tables
        """

    @abc.abstractmethod
    def get_table_by_name(self, table: str, db: str = '') -> 'ClickhouseTableModel':
        """
        system.tables
        see: https://clickhouse.com/docs/en/operations/system-tables/tables
        """

    @abc.abstractmethod
    def get_table_partitions(self, table: str, db: str = '') -> List[ClickhousePartitionModel]:
        """
        system.parts
        see: https://clickhouse.com/docs/en/operations/system-tables/parts
        """

    @abc.abstractmethod
    def get_processes(self) -> List[ClickhouseProcessModel]:
        """
        system.processes
        see: https://clickhouse.com/docs/en/operations/system-tables/processes
        """

    @abc.abstractmethod
    def get_process_by_query_id(self, query_id: str) -> ClickhouseProcessModel:
        """
        system.processes
        see: https://clickhouse.com/docs/en/operations/system-tables/processes
        """

    @abc.abstractmethod
    def get_disks(self) -> List[ClickhouseDiskModel]:
        """
        system.disks
        see: https://clickhouse.com/docs/en/operations/system-tables/disks
        """

    @abc.abstractmethod
    def get_table_columns(self, table: str, db: str = '') -> List[ClickhouseColumnModel]:
        """
        system.columns
        https://clickhouse.com/docs/en/operations/system-tables/columns
        """
