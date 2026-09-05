import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.command()
async def oi(ctx):
    await ctx.send("Salve!")

bot.run(os.getenv("TOKEN"))
