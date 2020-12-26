from discord.ext import commands
from config import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_MEME_SUBREDDITS, REDDIT_ADULT, REDDIT_ADULT_GIF, ADULT_NSFW_CHANNEL_ID
import random
import praw
import aiohttp
import discord

class adult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def prn(self, ctx):
        """Resim yada gif atar """
        #channel = ctx.get_channel(791740048273440768) jacking
        topıc = random.choice(REDDIT_ADULT)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit(topıc).hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def prngif(self, ctx):
        """gif yollar """
        #channel = ctx.get_channel(791740048273440768)
        gıfP = random.choice(REDDIT_ADULT_GIF)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit(gıfP).hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def prnbj(self, ctx):
        """Blowjob"""
        #channel = ctx.get_channel(791740048273440768) anal
        #gıfV = random.choice(REDDIT_ADULT_VID)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit('BlowJob').hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def pussy(self, ctx):
        """Amcıq atar """
        #channel = ctx.get_channel(791740048273440768)
        #topıc = random.choice(REDDIT_ADULT)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit('pussy').hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def prnanal(self, ctx):
        """Anal gif/resim atar """
        #channel = ctx.get_channel(791740048273440768)
        #topıc = random.choice(REDDIT_ADULT)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit('anal').hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def prncum(self, ctx):
        """Cumshot gif/resim atar"""
        #channel = ctx.get_channel(791740048273440768)
        #topıc = random.choice(REDDIT_ADULT)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit('cumshot').hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')
    @commands.command()
    async def hentai(self, ctx):
        """Cumshot gif/resim atar"""
        #channel = ctx.get_channel(791740048273440768)
        #topıc = random.choice(REDDIT_ADULT)
        if ctx.channel.id == ADULT_NSFW_CHANNEL_ID:
            async with ctx.channel.typing():
                reddit = praw.Reddit(client_id=REDDIT_APP_ID,
                client_secret=REDDIT_APP_SECRET,
                user_agent="Discord_Bot:%s:1.0" % REDDIT_APP_ID)
                memes_submissions = reddit.subreddit('hentai').hot()
                post_to_pick = random.randint(1, 10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in memes_submissions if not x.stickied)

                await ctx.send(submission.url)
        if ctx.channel.id != ADULT_NSFW_CHANNEL_ID:
            await ctx.send(f'Bu komut burda devre dışı!')



def setup(bot):
    bot.add_cog(adult(bot))