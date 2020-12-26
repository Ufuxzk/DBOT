from guard import bad_words
from discord.ext import commands
import discord


class function(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #  GUARD.PY DOSYASINDA Kİ BAD_WORDS LİSTESİNDE Kİ KÜFÜRLERİ ALGILADIĞINDA KANALDAN SİLER
    # BAD_WORDS LİSTESİNİ DİLEDİĞİNİZ KADAR ÇOĞALTABİLİRSİNİZ.
    # KÜFÜR ENGELLEYİCİYE İHTİYAÇ DUYMAZSANIZ EĞER FAKAT KOMUT DOSYASI KALSIN DERSENİZ TÜM KODLARIN BAŞINA HASHTAG GETİRİN  # VE SAVE ALIN
    # KALDIRAMAZSANIZ BU ÖZELLİĞİ BENİMLE İLETİŞİME GEÇİN --->>> ufuk@baslatbutonu.com <<<---

    @commands.Cog.listener()
    async def on_message(self,msg):
        filtered_words = bad_words
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()
       
        



def setup(bot):
    bot.add_cog(function(bot))