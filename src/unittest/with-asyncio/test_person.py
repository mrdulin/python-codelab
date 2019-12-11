import asyncio

import unittest
from unittest.mock import MagicMock

from person import Person


class TestPerson(unittest.TestCase):
    def test_create(self):
        """create person"""

        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)

        async def run_test():
            database_cursor = MagicMock()
            execute_stub = MagicMock(return_value='future result!')
            execute_coro = asyncio.coroutine(execute_stub)
            database_cursor.execute = execute_coro

            person = Person(name='mrdulin', cursor=database_cursor)
            person_create_response = await person.create()

            self.assertEqual(person_create_response, 'future result!')
            execute_stub.assert_called_once_with(person.insert_sql, ('mrdulin',))

        event_loop.run_until_complete(run_test())
        event_loop.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
