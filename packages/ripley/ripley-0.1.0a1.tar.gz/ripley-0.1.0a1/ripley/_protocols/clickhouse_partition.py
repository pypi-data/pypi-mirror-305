import abc

from .clickhouse_on_cluster import ClickhouseOnClusterProtocol
from ..clickhouse_models.table import ClickhouseTableModel as CTable


class ClickhousePartitionProtocol(ClickhouseOnClusterProtocol, metaclass=abc.ABCMeta):
    """
    see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition
    """
    @abc.abstractmethod
    def move_partition(self, from_table: CTable, to_table: CTable, partition: str) -> None:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#move-partition-to-table
        """

    @abc.abstractmethod
    def replace_partition(self, from_table: CTable, to_table: CTable, partition: str) -> None:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#replace-partition
        """

    @abc.abstractmethod
    def drop_partition(self, table: CTable, partition: str) -> None:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#drop-partitionpart
        """

    @abc.abstractmethod
    def detach_partition(self, table: CTable, partition: str) -> None:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#detach-partitionpart
        """

    @abc.abstractmethod
    def attach_partition(self, table: CTable, partition: str) -> None:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#attach-partitionpart
        """
