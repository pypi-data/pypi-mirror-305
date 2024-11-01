import abc

from .clickhouse_on_cluster import ClickhouseOnClusterProtocol
from ..clickhouse_models.db import ClickhouseDbModel


class ClickhouseDbProtocol(ClickhouseOnClusterProtocol, metaclass=abc.ABCMeta):
    """
    Database operations
    """
    @abc.abstractmethod
    def create_db(self, name: str, on_cluster: str = '', engine: str = '') -> ClickhouseDbModel:
        """
        see: https://clickhouse.com/docs/en/sql-reference/statements/create/database
        """
