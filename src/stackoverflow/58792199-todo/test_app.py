import asyncio
import pytest
import unittest
from unittest.mock import MagicMock, patch
from app import Application


@pytest.mark.asyncio
async def test_func1():
    app = Application()
    func2_stub = MagicMock(return_value='future result!')
    func2_coro = asyncio.coroutine(func2_stub)

    async with patch.object(Application, 'func2', return_value=func2_coro) as mock:
        res = await app.func1()
        print(res)
        # mock.assert_awaited_with(app.func3())
