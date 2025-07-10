import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ NotifyHub is online as {bot.user}!")

@bot.command()
async def ping(ctx):
    await ctx.send("📡 Pong! NotifyHub aktif.")

@bot.command()
async def about(ctx):
    await ctx.send("🔔 Aku adalah NotifyHub, bot all-in-one notifier buatan VoltoCraft!")

bot.run(os.getenv("TOKEN"))
