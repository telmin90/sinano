import discord
from discord.ext import commands
from datetime import datetime, timedelta


class Messege(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # 直近にどのメンバーが書き込んだのかを表示する
    @commands.command()
    async def member(self, ctx, number:int=6):
        if 1 <= number <= 24:
            now = datetime.now()
            gap = now - timedelta(hours=number)
            member_dic = {}
            guild = ctx.guild
            
            for channel in guild.text_channels:
                async for message in channel.history(limit=None, after=gap):
                    if message.author.display_name in member_dic:
                        member_dic[message.author.display_name] += 1
                    else:
                        member_dic[message.author.display_name] = 1
            
            await ctx.send(f"{member_dic}")
        
        else:
            await ctx.send("1から24までの数字を入れてください")
            
async def setup(bot):
    await bot.add_cog(Messege(bot))