from discord.ext import commands
from dictionary import Dictionary
import discord

dictionary = Dictionary()

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def dict(self, ctx, term: str):
        message = ctx.message
        res = dictionary.get_definitions_for(term)
        if not 'message' in res:
            word = res[0]['word']
            meaning = res[0]['meanings'][0]['definitions'][0]['definition']
            part = res[0]['meanings'][0]['partOfSpeech']
            await message.channel.send(
                embed=discord.Embed(
                    title=word,
                    description=meaning
                )
            )
        else:
            await message.channel.send(f'Could not find definition for term `{term}`.')
