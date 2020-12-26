

'''
  _____                 _                      _   ____          _    _  __            _          
 |  __ \               | |                    | | |  _ \        | |  | |/ _|          | |         
 | |  | | _____   _____| | ___  _ __   ___  __| | | |_) |_   _  | |  | | |_ _   _  ___| | ____  __
 | |  | |/ _ \ \ / / _ \ |/ _ \| '_ \ / _ \/ _` | |  _ <| | | | | |  | |  _| | | |/ __| |/ /\ \/ /
 | |__| |  __/\ V /  __/ | (_) | |_) |  __/ (_| | | |_) | |_| | | |__| | | | |_| | (__|   <  >  < 
 |_____/ \___| \_/ \___|_|\___/| .__/ \___|\__,_| |____/ \__, |  \____/|_|  \__,_|\___|_|\_\/_/\_\
                               | |                        __/ |                                   
                               |_|                       |___/                                   


'''





import discord
import os
import random
import json
from itertools import cycle
from config import Bot_token, Prefıx, Owner, BOT_ID
from discord.ext import commands, tasks
from guard import bad_words


bot = commands.Bot(command_prefix=Prefıx)
status = cycle(['Spotify','!!yardım', '!!adulthelp', 'developed by ufuck',])
# status = cycle(['Spotify','!!yardım', '!!adulthelp']) #BOTUN AKTİVİTE DURUMU  DEĞİŞTİREBİLİRSİNİZ
bot.remove_command('help') # SİLME YARDIM KOMUTU ÇALIŞIR FAKAT DEFAULT HELP KOMUTU AKTİF OLUR



@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user} has logged in.')
    #bot.load_extension('cogs.pıng')





# @bot.event
# async def on_message(message):
#     response = [
#     'as', 
#     'cami mi lan burası',
#     'selam canım', 
#     'bak şuraya kimler gelmiş!',
#     'Efendiler teşrif etmiş,as'
# ]
#     if message.author == bot.user:
#         return

#     if message.content == 'sa':
#         await message.channel.send(f'{random.choice(response)}, {message.author.mention}')
        

@tasks.loop(seconds=10)
async def change_status():
	await bot.change_presence(
        activity= discord.Activity(
            type= discord.ActivityType.listening,
             name=next(status)
        )
    )



@bot.event
async def on_message(message):
    if not message.author.bot:
        print('function load')
        with open('users.json','r', encoding=('utf8')) as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 0.2, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('users.json','w') as f:
            json.dump(users, f)
    await bot.process_commands(message)




async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != BOT_ID:
    if lvl_start < lvl_end:
      await channel.send('{} Level up! {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@bot.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('users.json','r',encoding=('utf8')) as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = 0x00ffaa)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('users.json','r',encoding=('utf8')) as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = 0x00ffaa)
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)

@bot.command(aliases=['lb'])
async def leaderboard(ctx, x=10):
  with open('users.json', 'r',encoding=('utf8')) as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  
  for user in list(users[str(ctx.guild.id)]):
    name = int(user)
    total_amt = users[str(ctx.guild.id)][str(user)]['experience']
    leaderboard[total_amt] = name
    total.append(total_amt)
    

  total = sorted(total,reverse=True)
  

  em = discord.Embed(
    title = f'{ctx.guild.name} Top {x} Leaderboard',
    description = 'Sunucuda ki en yüksek seviyeye sahip kullanıcılar'
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    member = bot.get_user(id_)
    
    # em.set_thumbnail(url=ctx.guild.icon_url)
    em.add_field(name = f'{index}: {member}', value = f'{amt}', inline=False)
    # em.set_footer(text=ctx.guild.name)
    
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = em)


def is_it_me(ctx):
    	return ctx.author.id ==  Owner


@bot.command()
@commands.check(is_it_me)
async def dev(ctx):
    await ctx.send(f'Merhaba, benim geliştiricim = {ctx.author.mention}.')



@bot.command()
@commands.check(is_it_me)
async def yükle(ctx, extension):
    """İstenilen,komut dosyalarını yükler."""
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Komutlar başarıyla yüklendi {ctx.author}')


@bot.command()
@commands.check(is_it_me)
async def kaldır(ctx, extension):
    """Komut dosyalarını yüklenmesini iptal eder."""
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Komutlar başarıyla kaldırıldı {ctx.author}')

@bot.command()
@commands.check(is_it_me)
async def yenile(ctx, extension):
    """ İstenilen komut dosyasını yeniler."""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Komutlar başarıyla yenilendi {ctx.author}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')







bot.run(Bot_token)