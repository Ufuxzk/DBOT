import discord
import random
from discord.ext import commands

class genel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Genel komutların yüklenmesi başarılı')

    @commands.Cog.listener()
    async def on_message(self, message):
        #self.message = message
        response = [ 'as', 'cami mi lan burası', 'selam canım', 'bak sen kimler gelmiş kimler!', 'Efendiler teşrif etmiş,as']
        if message.author == self.bot.user:
            return
        if message.content == 'sa':
            await message.channel.send(f'{random.choice(response)}, {message.author.mention}')

    @commands.command()
    async def avatar(self, ctx, *, avamember: discord.Member=None):
        """istenilen kullanıcının profil resmini atar."""
        embed = discord.Embed(
            color=0x00ffaa,
            timestamp=ctx.message.created_at,
            title=f'Avatar : {avamember}'
        )
        embed.set_image(

             url='{}'.format(avamember.avatar_url)
        )
        embed.set_footer(
            text= f'{ctx.author} tarafından istendi'
            #text = '{} tarafından istendi'.format(ctx.author)
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def infouser(self, ctx, *, member: discord.Member=None):
        """Etiketlenen kullanıcının bilgisini atar(etiket atmazsanız kendi bilginizi atar)."""
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.green(), timestamp=ctx.message.created_at,
                          title=f"Kullanıcı bilgisi - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{ctx.author} tarafından oluşturuldu.")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Görünen adı:", value=member.display_name)

        embed.add_field(name="Hesap oluşturma tarihi:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Sunucuya katılma tarihi:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Rolleri:", value="".join([role.mention for role in member.roles[1:]]))
        embed.add_field(name="En yüksek rolü:", value=member.top_role.mention)
        print(member.top_role.mention)
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def cls(self, ctx, amount : int):
        """Girilen miktarda mesajı siler"""
        await ctx.channel.purge(limit=amount)
        await ctx.send('Mesajlar silindi', delete_after=5)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx,):
        """1000 adet mesaj siler."""
        await ctx.channel.purge(limit=1000)
        await ctx.send(f'Sohbet temizlendi!', delete_after=5)





def setup(bot):
    bot.add_cog(genel(bot))