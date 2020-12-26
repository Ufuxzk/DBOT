import discord
import datetime
from discord.ext import commands
from config import Owner


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    def is_it_me(self, ctx):
        return ctx.author.id ==  Owner

    @commands.command()
    @commands.check(is_it_me)
    async def status(self, ctx, *args):
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        embed = discord.Embed(description="Server Status",
        color=0x00ffaa)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        #embed.set_image(url="")
        embed.add_field(name="Server Name",
        value=guild.name, inline=False)

        embed.add_field(name="# Voice channels",
        value=no_voice_channels)

        embed.add_field(name="# Text channels",
        value=no_text_channels)

        embed.set_author(name=self.bot.user.name)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Admin(bot))