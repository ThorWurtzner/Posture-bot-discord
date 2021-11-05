# The first step in implementing your bot user is to create a connection to Discord. With discord.py, you do this by creating an instance of Client:
# A Client is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs.

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run(TOKEN)