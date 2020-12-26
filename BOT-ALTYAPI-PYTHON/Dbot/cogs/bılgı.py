from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup




class Döviz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dolar(self, ctx):     
        r = requests.get("https://www.bloomberght.com/")
        soup = BeautifulSoup(r.content, "html.parser")
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        dolar = veri[1].text
        embed = discord.Embed(title='Döviz', color=0x00ffaa)
        embed.set_thumbnail(url="https://i.imgur.com/ySNHBNA.png")
        embed.add_field(name='Dolar', value=dolar + '₺', inline=False)
        embed.set_footer(text='💸💸💸💸')
        await ctx.send(embed=embed)
    @commands.command()
    async def gram(self, ctx):
        r = requests.get("https://altin.in/")
        soup = BeautifulSoup(r.content, "html.parser")
        alıs = soup.find_all('li',attrs={'class':'midrow alis'})
        satıs = soup.find_all('li',attrs={'class':'midrow satis'})
        GRAM_ALIS = alıs[0].text
        GRAM_SATIS = satıs[0].text
        embed =  discord.Embed(title='Döviz', color=0x00ffaa)
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/economy-color-v-1/512/bar_brick_finance_gold_goldbrick_lingot-512.png")

        embed.add_field(name='Gram altın alış', value=GRAM_ALIS + '₺')
        embed.add_field(name='Gram altın satış', value=GRAM_SATIS + '₺')

        await ctx.send(embed=embed)
    @commands.command()
    async def çeyrek(self, ctx):
        r = requests.get("https://altin.in/")
        soup = BeautifulSoup(r.content, "html.parser")
        alıs = soup.find_all('li',attrs={'class':'midrow alis'})
        satıs = soup.find_all('li',attrs={'class':'midrow satis'})
        ÇEYREK_ALIS = alıs[1].text
        ÇEYREK_SATIS = satıs[1].text
        embed =  discord.Embed(title='Döviz', color=0x00ffaa)
        embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/economy-color-v-1/512/bar_brick_finance_gold_goldbrick_lingot-512.png")

        embed.add_field(name="Çeyrek altın alış", value=ÇEYREK_ALIS + '₺')
        embed.add_field(name="Çeyrek altın satış", value=ÇEYREK_SATIS + '₺')

        await ctx.send(embed=embed)
    @commands.command()
    async def euro(self, ctx):
        r = requests.get("https://www.bloomberght.com/")
        soup = BeautifulSoup(r.content, "html.parser")
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        euro = veri[2].text
        embed = discord.Embed(title='Döviz', color=0x00ffaa)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl5Sn7IMg4RutKvGk9ftOTXnh37AfloYRPUQ&usqp=CAU")
        embed.add_field(name='Euro', value=euro + '₺')
        embed.set_footer(text='💸💸💸💸')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Döviz(bot))