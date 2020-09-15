from discord.ext import commands
from disputils import BotEmbedPaginator
from discord import Embed
from dictionary import Dictionary

dictionary = Dictionary()


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dict(self, ctx, term: str):
        message = ctx.message
        res = dictionary.get_definitions_for(term)
        if not "message" in res:
            data = res[0]
            meaning = res[0]["meanings"][0]["definitions"][0]["definition"]
            part = res[0]["meanings"][0]["partOfSpeech"]

            meanings = []
            count = len(data["meanings"])
            for meaning in data["meanings"]:
                pos = meaning["partOfSpeech"]
                definitions = ""
                for defi in meaning["definitions"]:
                    definitions += ' - ' + defi["definition"] + '\n\n'
                meanings.append(
                    Embed(title=data['word'],
                    description=f'```{definitions}```',
                    color=0x115599)
                )
            
            paginator = BotEmbedPaginator(ctx, meanings)
            await paginator.run()

        else:
            await message.channel.send(f"Could not find definition for term `{term}`.")
