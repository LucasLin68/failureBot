import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio
from flask import Flask
from threading import Thread


load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True

bot = commands.Bot(command_prefix = '!', intents = intents)

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(filename)
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def sync(ctx):
    bot.tree.copy_global_to(guild = ctx.guild)
    synced = await bot.tree.sync(guild = ctx.guild)
    await ctx.send("synced")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "bot" in message.content.lower() and "hi" in message.content.lower():
        await message.channel.send(f"Hi {message.author.display_name}!")
        
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
  await ctx.send(f"你好啊{ctx.author.mention}")

async def main():
    async with bot:
        await bot.start(token)

app = Flask('')

@app.route('/')
def home():
    return "上線了"

def run_flask():
  
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

async def main():
   
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
 
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__ == '__main__':
  	asyncio.run(main())
