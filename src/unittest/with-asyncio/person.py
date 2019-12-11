class Person:
    def __init__(self, name=None, cursor=None):
        self.name = name
        self.cursor = cursor
        self.insert_sql = 'insert into person values ?;'

    async def create(self):
        """create person"""
        return await self.cursor.execute(self.insert_sql, (self.name,))
