import discord
from discord.ext import commands
from datetime import datetime, timedelta
from config import *


class Messege(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # 直近にどのメンバーが書き込んだのかを表示する
    @commands.command()
    async def member(self, ctx, number:int=6):
        if 1 <= number <= 24:
            now = datetime.now()
            gap = now - timedelta(hours=number)
            members = {}
            description = ""
            guild = ctx.guild
            
            for channel in guild.text_channels:
                async for message in channel.history(limit=None, after=gap):
                    if message.author.display_name in members:
                        members[message.author.display_name] += 1
                    else:
                        members[message.author.display_name] = 1
            
            members_sorted = sorted(members.items(), key=lambda x:x[1], reverse=True)
            for i in members_sorted:
                description += f"{i[0]} ({i[1]}), "
            
            embed = discord.Embed(
                title = f"{number}時間以内に{len(members)}人が書き込みをしました",
                description = f"**{description}**",
                color = Color.BANNER
            )
            
            await ctx.send(embed=embed)
        
        else:
            await ctx.send("1から24までの数字を入れてください")
            
async def setup(bot):
    await bot.add_cog(Messege(bot))