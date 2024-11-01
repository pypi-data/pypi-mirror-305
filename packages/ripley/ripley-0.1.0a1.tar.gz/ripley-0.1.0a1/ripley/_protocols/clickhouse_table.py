import abc

from .clickhouse_on_cluster import ClickhouseOnClusterProtocol
from .clickhouse_settings import ClickhouseSettingsProtocol
from ..clickhouse_models.s3_settings import ClickhouseS3SettingsModel
from ..clickhouse_models.table import ClickhouseTableModel


class ClickhouseTableProtocol(ClickhouseSettingsProtocol, ClickhouseOnClusterProtocol, metaclass=abc.ABCMeta):
    """
    Table operations
    """
    @abc.abstractmethod
    def create_table_as(
        self,
        from_table: ClickhouseTableModel,
        table: str,
        db: str = '',
        order_by: list = None,
        partition_by: list = None,
        engine: str = '',
    ) -> ClickhouseTableModel:
        """
        Creates a table with the same structure or with custom ORDER BY / PARTITION BY / Engine
        """

    @abc.abstractmethod
    def insert_from_table(self, from_table: ClickhouseTableModel, to_table: ClickhouseTableModel) -> None:
        """
        INSERT INTO db1.table1 SELECT * FROM db2.table2
        """

    @abc.abstractmethod
    def truncate(self, table: str, db: str = '') -> None:
        pass

    @abc.abstractmethod
    def insert_from_s3(self, table: ClickhouseTableModel, s3_settings: ClickhouseS3SettingsModel):
        """
        INSERT INTO db1.table1 SELECT * FROM s3(...)

        see: https://clickhouse.com/docs/en/integrations/s3#testing-1
        """

    @abc.abstractmethod
    def insert_table_to_s3(self, table: ClickhouseTableModel, s3_settings: ClickhouseS3SettingsModel):
        """
        INSERT INTO FUNCTION s3(...) SELECT * FROM {db}.{table}

        see: https://clickhouse.com/docs/en/integrations/s3#exporting-data
        """

    @abc.abstractmethod
    def rename_table(self, table: ClickhouseTableModel, new_name: str, db: str = '') -> None:
        """
        https://clickhouse.com/docs/en/sql-reference/statements/rename
        """
