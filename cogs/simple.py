import discord
from discord.ext import commands
import datetime
from config import *


# 処理が単純なコマンドをこのクラスで管理している
class SimpleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latency_ms = round(latency * 1000)
        await ctx.send(f"Pong!\n**Latency**: {latency_ms}ms")
    
    # eval()はセキュリティ的に危ないらしい
    @commands.command()
    async def cal(self, ctx, *, formula:str):
        try:
            result = str(eval(formula))
            await ctx.send(f"{formula} = {result}")
        except Exception as e:
            embed = discord.Embed(description=f"{e}", color=Color.ERROR)
            await ctx.send(embed=embed)
    
    
        
async def setup(bot):
    await bot.add_cog(SimpleCommands(bot))