import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if message.content.startswith('hehe'):
            i = random.randrange(1,14)
            await message.channel.send(file=discord.File(str(i)+'.jpg'))
client = MyClient()
client.run('')
