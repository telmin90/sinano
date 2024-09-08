import discord
from discord.ext import commands
import datetime
from config import *


class Mokou(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # リンク集
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
    
    # 生存日数をカウント
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
    
    # 誕生日までの日数をカウント
    @commands.command()
    async def birthday(self, ctx):
        birthday = [11, 15]
        today = datetime.datetime.now().date()
        text = ""
        
        # 残り日数を返す関数
        def return_days(today):
            if (today.month, today.day) > (birthday[0], birthday[1]):
                next_birthday = datetime.date(today.year + 1, birthday[0], birthday[1])
            else:
                next_birthday = datetime.date(today.year, birthday[0], birthday[1])
            limit = (next_birthday - today).days
            return limit
        
        remaining = return_days(today)
        if remaining == 0:
            text = "今日はもこうの誕生日です"
        elif remaining == 1:
            text = "明日はもこうの誕生日です"
        else:
            text = f"もこうの誕生日まであと{remaining}日です"
        
        await ctx.send(embed = discord.Embed(description=text, color=Color.BANNER))


async def setup(bot):
    await bot.add_cog(Mokou(bot))