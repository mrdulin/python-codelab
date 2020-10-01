from unittest.mock import Mock
from code_53856568 import coroutine_creater
import pytest


@pytest.mark.asyncio
async def test_test():
    def coroutine_creater_side_effect():
        return coroutine_creater(5)

    my_mock = Mock(side_effect=coroutine_creater_side_effect)

    first_call = await my_mock()
    second_call = await my_mock()

    assert first_call == 5, 'first call failed'
    assert second_call == 5, 'second call failed'
