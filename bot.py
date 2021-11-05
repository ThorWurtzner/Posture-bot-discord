# The first step in implementing your bot user is to create a connection to Discord. With discord.py, you do this by creating an instance of Client:
# A Client is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs.

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    # guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == "sindri": 
        await message.channel.send("er en faggot ez")

    if message.content == "/help":
        await message.channel.send("nej")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hej {member.name}, Velkommen til serveren!')

client.run(TOKEN)