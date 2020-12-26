import discord 
from discord.ext import commands
# from AntiSpam import AntiSpamHandler


class moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # self.bot.handler = AntiSpamHandler(bot)

    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Moderasyon komutları yüklendi!')
    # @commands.Cog.listener()
    # async def on_message(message):
    #     self.bot.handler.propagate(message)
    #     await bot.process_commands(message)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has kicked.', delete_after=5)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            await ctx.send('Cant ban Moderators/Admins')
        else:
            await member.ban(reason=reason)
            await ctx.send(f'{user.mention} has been banned!')



    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(789868282034520064)
        await member.add_roles(muted_role)
        await ctx.send(member.mention + {ctx.author} + " tarafından susturuldu!", delete_after=5)
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(789868282034520064)
        await member.remove_roles(muted_role)
        await ctx.send(member.mention + {ctx.author} + " tarafından susturması kaldırıldı!", delete_after=5)
    




    # @commands.command()
    # @commands.has_permissions(manage_channels=True)
    # async def chlock(self, ctx, channel : discord.TextChannel=None):
    #     channel = channel or ctx.channel
    #     overwrite = channel.overwrites_for(ctx.guild.default_role)
    #     overwrite.send_messages = False
    #     await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    #     await ctx.send('Channel locked.')

def setup(bot):
    bot.add_cog(moderation(bot))