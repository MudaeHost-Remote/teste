import selfcord

token = "OTUzMDkzOTkyMTAxMzQ3Mzg4.G1i7Ot.AS1xM7nAGxgmkn4_nbDrxTlnd_Z4FwQs5SA4ng"
channelid = 1322603701222772776

class MyClient(selfcord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.channel.id == channelid:
            await message.channel.send('Hello World')

client = MyClient()
client.run(token)
