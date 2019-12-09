import types
import unittest


def function():
    """普通函数"""
    return 1


def generator():
    """生成器函数"""
    yield 1


async def async_function():
    """异步函数（协程）"""
    return 1


async def async_generator():
    """异步生成器"""
    yield 1


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def await_coroutine():
    return await async_function()


class TestEx01(unittest.TestCase):
    def test_types(self):
        self.assertIs(type(function), types.FunctionType)
        self.assertIs(type(generator()), types.GeneratorType)
        self.assertIs(type(async_function()), types.CoroutineType)
        self.assertIs(type(async_generator()), types.AsyncGeneratorType)

    def test_await_coroutine(self):
        res = run(await_coroutine())
        self.assertEqual(res, 1)


unittest.main()
