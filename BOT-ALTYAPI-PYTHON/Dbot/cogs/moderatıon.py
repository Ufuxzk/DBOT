import discord 
from discord.ext import commands
# from AntiSpam import AntiSpamHandler


class moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Moderasyon komutları yüklendi!')
 


    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(789868282034520064) # <--- buraya sunucunuzda bir MUTE ROLÜ BELİRLEYİN VE O ROLÜN İD'SİNİ GİRİN AYNI İD Yİ AŞAĞIDA Kİ UNMUTE İÇİNDE YAPIN.
        await member.add_roles(muted_role)
        await ctx.send(member.mention + {ctx.author} + " tarafından susturuldu!", delete_after=5)
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(789868282034520064)
        await member.remove_roles(muted_role)
        await ctx.send(member.mention + {ctx.author} + " tarafından susturması kaldırıldı!", delete_after=5)
    




def setup(bot):
    bot.add_cog(moderation(bot))
