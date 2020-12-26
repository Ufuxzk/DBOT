import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Pıng komutu yüklemesi başarılı!')


    @commands.command()
    async def pıng(self, ctx):
        """TEST."""
        embed = discord.Embed(
            color=0x00ffaa,
            title="Pıng",
        )
        embed.add_field(
            name="test",
            value=round(self.bot.latency * 1000)
        )
        embed.set_footer(
            text=f'{ctx.author} tarafından oluşturuldu'
            #text="{} tarafından oluşturuldu".format(ctx.author)
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(test(bot))
