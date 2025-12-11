import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True

bot = commands.Bot(command_prefix = '!', intents = intents)

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def sync(ctx):
    bot.tree.copy_global_to(guild = ctx.guild)
    synced = await bot.tree.sync(guild = ctx.guild)
    await ctx.send("synced")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

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
        await load_extensions()
        await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())

bot.run(token)
