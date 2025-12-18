import discord
from discord import app_commands
from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            return
       
        if "bot" in message.content.lower() and "hi" in message.content.lower():
            await message.channel.send(f"你好 {message.author.display_name}!")
    
async def setup(bot):
    await bot.add_cog(OnMessage(bot))
