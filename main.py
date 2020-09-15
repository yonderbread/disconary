import discord
from utils import Config
from commands import Commands

class Client(discord.ext.commands.Bot):
    async def on_ready(self):
        self.add_cog(Commands(self))
        print('Started.')

config = Config()
config.load()

client = Client(command_prefix='!')
client.run(config.contents["token"])

