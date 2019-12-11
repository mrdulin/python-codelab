import asyncio


class Application:
    async def func1(self):
        return await self.func2()

    async def func2(self):
        return 1

    async def func3(self):
        pass


app = Application()

print(asyncio.run(app.func1()))
