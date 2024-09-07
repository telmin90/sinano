import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import config


# tokenの読み込み
load_dotenv()
TOKEN = os.environ['BOT_TOKEN']

# botの初期化
intents = discord.Intents.default()
intents.message_content = True
#intents.guilds = True
#intents.messages = True
#intents.members = True 

bot = commands.Bot(command_prefix='>', intents=intents)

# ログイン完了のメッセージ
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# cogの読み込み
@bot.event
async def setup_hook():
    for cog in config.__cogs__:
        await bot.load_extension(cog)

# botテスト用のコマンド
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await bot.process_commands(message)



if __name__ == '__main__':
    bot.run(TOKEN)