import asyncio
import websockets
import json
import datetime


def json_default(value):
    try:
        return value.__dict__
    except AttributeError:
        pass


class NetworkTool:
    def __init__(self, bot):
        self.bot = bot

    async def hello(self, websocket, path):
        msg = await websocket.recv()
        if msg == "hello":
            await websocket.send("hello")
            print("> {}".format("hello"))
        elif msg == "bot":
            await websocket.send(json.dumps(self.bot, default=json_default))
            print("> {}".format(json.dumps(self.bot, default=json_default)))


# test
def setup(bot):
    n = NetworkTool(bot)

    asyncio.get_event_loop().run_until_complete(websockets.serve(n.hello, 'localhost', 8777))

    bot.add_cog(n)
