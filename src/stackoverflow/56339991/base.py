from util import Util as u


class BaseImporter:

    __source = None
    __table_name = None
    __folder_name = None

    def __init__(self, folder_name: str, source: str, table: str) -> None:
        self.__source = source
        self.__table_name = table
        self.__folder_name = folder_name

    def run_importer(self):
        data = u.get_data_from_external_source(self.__source)
        u.create_n_insert_into_sql(self.__table_name, data)
        u.create_n_insert_into_hive(self.__table_name, data)
        u.create_folder_hdfs(self.__folder_name)
