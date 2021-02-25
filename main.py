import os
import discord
from discord.ext import commands
import keep_alive
import random
import json
import asyncio
import aiohttp

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, case_insensitive=True)

async def status():
    while True:
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(client. guilds)} servers!"))
            await asyncio.sleep(5)
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="@ANDR3W help"))
            await asyncio.sleep(5)

@client.event
async def on_ready():
        print(f'{client.user.name}#{client.user.discriminator} is now running!')
        await client.loop.create_task(status())

keep_alive.keep_alive()
token = os.environ.get("TOKEN")
client.run(token)