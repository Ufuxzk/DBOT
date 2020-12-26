from discord.ext import commands
import discord


class navigate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def yardım(self, ctx):
        embed = discord.Embed(
		colour = 0x00ffaa,
		timestamp=ctx.message.created_at,
		title=f"Komut listesi"
	    )
        embed.set_footer(text=f"{ctx.author} tarafından oluşturuldu.")

        embed.set_author(name='Yardım')
        embed.add_field(name='!!pıng', value='Botun ping değerini söyler', inline=True)
        embed.add_field(name='!!cls', value='belirtilen miktarda mesajı siler -> !!cls <miktar>', inline=True)
        embed.add_field(name='!!avatar', value='Etiketlenen kullanıcın resmini gösterir -> !!avatar @mention yada !!avatar ', inline=True)
        embed.add_field(name='!!meme', value='Redditten rastgele gönderi atar', inline=True)
        embed.add_field(name='!!infouser', value='İstenilen kullanıcın bilgilerini verir -> !!infouser @mention yada !!infouser', inline=True)
        embed.add_field(name='!!dev', value='Botun geliştiricisini söyler -> Sadece geliştirici kullanabilir!', inline=True)
        embed.add_field(name='!!purge', value='1000 adet mesaj siler!', inline=True)
        embed.add_field(name='!!kick', value='***(YALNIZ YÖNETİCİLER)***', inline=True)
        embed.add_field(name='!!mute', value='***(YALNIZ YÖNETİCİLER)*** hedef kullanıcıyı susturur -> !!mute @mention', inline=True)
        embed.add_field(name='!!unmute', value='***(YALNIZ YÖNETİCİLER)*** kullanıcın susturmasını kaldırır -> !!unmute @mention', inline=True)
        embed.add_field(name='!!ban', value='***(YALNIZ YÖNETİCİLER)*** kullanıcın susturmasını kaldırır -> !!ban @mention', inline=True)
        embed.add_field(name='!!dolar', value='güncel dolar fiyatını söyler -> !!dolar', inline=True)
        embed.add_field(name='!!euro', value='güncel euro fiyatını söyler -> !!euro ', inline=True)
        embed.add_field(name='!!gram', value='güncel gram altın fiyatını söyler  -> !!gram', inline=True)
        embed.add_field(name='!!çeyrek', value='güncel çeyrek altın fiyatını söyler   -> !!çeyrek', inline=True)
        embed.add_field(name='!!level', value='Seviyenizi söyler -> !!level', inline=True)
        embed.add_field(name='!!leaderboard  or !lb', value='Sunucu level sıralaması -> !!lb ', inline=True)
        embed.add_field(name='!!yükle', value='***YALNIZCA GELİŞTİRİCİ*** Komutları yükler  -> !!yükle', inline=True)
        embed.add_field(name='!!kaldır', value='***YALNIZCA GELİŞTİRİCİ*** Komutları kaldırır  -> !!kaldır', inline=True)
        embed.add_field(name='!!yenile', value='***YALNIZCA GELİŞTİRİCİ*** Komutları yeniler  -> !!yenile', inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def adulthelp(self, ctx):
        embed = discord.Embed(
		colour = 0x00ffaa,
		timestamp=ctx.message.created_at,
		title=f"Adult/NSFW komut listesi YALNIZCA NSFW KANALINDA GEÇERLİDİR!"
	    )
        embed.set_footer(text=f"{ctx.author} tarafından oluşturuldu.")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/db/IFCO_18_%28Cinema%29.png")

        embed.set_author(name='Adult yardım')
        embed.add_field(name='!!prn', value='+18 resim atar -> !!prn', inline=True)
        embed.add_field(name='!!prngif', value='+18 gif atar -> !!prngif', inline=True)
        embed.add_field(name='!!prnanal', value='+18 anal gif/resim atar -> !!prnanal', inline=True)
        embed.add_field(name='!!prnbj', value='+18 bj gif/resim atar', inline=True)
        embed.add_field(name='!!prncum', value='+18 cum gif/resim atar -> !!prncum', inline=True)
        embed.add_field(name='!!pussy', value='+18 vajina gif/resim atar -> !!pussy', inline=True)
        embed.add_field(name='!!hentai', value='hentai gif/resim atar -> !!hentai', inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(navigate(bot))