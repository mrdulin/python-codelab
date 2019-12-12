from base import BaseImporter


class ChildImporter(BaseImporter):

    def __init__(self, folder_name: str, source: str, table: str):
        super().__init__(
            folder_name='my_folder',
            source='mysql',
            table='accounts',
        )
