import discord
from discord.ext import commands
import datetime
from config import *


class Mokou(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mokou(self, ctx):
        embed=discord.Embed(title="もこう", color=Color.BANNER)
        embed.add_field(name="Youtube", value="https://www.youtube.com/@mokoustream", inline=True)
        embed.add_field(name="X", value="https://x.com/mokouliszt", inline=True)
        embed.add_field(name="Instagram", value="https://www.instagram.com/mokouliszt/", inline=True)
        embed.add_field(name="ニコニコ", value="https://ch.nicovideo.jp/mokou1", inline=True)
        embed.add_field(name="ツイキャス", value="https://twitcasting.tv/mokouliszt/", inline=True)
        embed.add_field(name="Twitch", value="https://www.twitch.tv/mokouliszt1", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def lifetime(self, ctx):
        mokou_birth = datetime.date(1990,11,15)
        today = datetime.date.today()
        day_difference = (today - mokou_birth).days
        embed = discord.Embed(
                description = f"もこうが生まれた日から**{day_difference}**日が経過しました",
                color = Color.BANNER
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Mokou(bot))