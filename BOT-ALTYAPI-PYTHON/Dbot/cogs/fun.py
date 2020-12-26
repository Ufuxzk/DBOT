import aiohttp
from discord.ext import commands
import discord
import random
import praw

from config import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_MEME_SUBREDDITS, MEME_CHANNEL_ID


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.reddit = None
        # if REDDIT_APP_ID and REDDIT_APP_SECRET:
        #     self.reddit = praw.Reddit(client_id=REDDIT_APP_ID,
        #     client_secret=REDDIT_APP_SECRET, user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == MEME_CHANNEL_ID:
            if message.content == 'https://images-ext-2.discordapp.net/external/YIl0SOtr-NUhtXuWW92I72dYb1SLkuCL1IvGFGDN1l8/https/i.redd.it/lskulk4fu9761.jpg?width=708&height=498':
                await message.delete()
            else:
                return


        

    @commands.command()
    async def meme(self, ctx):
        #channel = ctx.get_channel(791740048273440768)
        topıc = random.choice(REDDIT_ENABLED_MEME_SUBREDDITS)
        if ctx.channel.id == MEME_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit(topıc).hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != MEME_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')

    # @commands.command()
    # async def rand(self, ctx, subreddit: str = ""):
    #     async with ctx.channel.typing():
    #         if self.reddit:
    #             #start working
    #             chosen_subreddit =  REDDIT_ENABLED_MEME_SUBREDDITS[0]
    #             if not subreddit:
    #                 #should take default one
    #                 if subreddit in REDDIT_ENABLED_MEME_SUBREDDITS:
    #                     chosen_subreddit = subreddit

    #             submissions = self.reddit.subreddit(chosen_subreddit).hot()
                
    #             post_to_pick = random.randint(1,10)
    #             for i in range(0, post_to_pick):
    #                 submissions = next(x for x in submissions if not x.stickied)
    #             await ctx.send(submission.url)

    #         else:
    #             await ctx.send("This is not working. Contact Developer")


def setup(bot):
    bot.add_cog(Fun(bot))