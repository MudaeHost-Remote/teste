import selfcord
import os

token = os.getenv("TOKEN")
channelid = 1322603701222772776

class MyClient(selfcord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.channel.id == channelid:
            await message.channel.send('Hello World')

client = MyClient()
client.run(token)
