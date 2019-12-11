import asyncio
import pytest
from unittest.mock import MagicMock

from person import Person


class TestPerson:
    @pytest.mark.asyncio
    async def test_create(self):
        database_cursor = MagicMock()
        execute_stub = MagicMock(return_value='future result!')
        execute_coro = asyncio.coroutine(execute_stub)
        database_cursor.execute = execute_coro

        person = Person(name='mrdulin', cursor=database_cursor)
        person_create_response = await person.create()

        assert person_create_response == 'future result!'
        execute_stub.assert_called_once_with(person.insert_sql, ('mrdulin',))
