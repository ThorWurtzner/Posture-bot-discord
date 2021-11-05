# The first step in implementing your bot user is to create a connection to Discord. With discord.py, you do this by creating an instance of Client:
# A Client is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs.

import os
import discord

from threading import Timer

from discord.ext import commands
from discord import FFmpegPCMAudio

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()

# @client.event
# async def on_ready():
#     # guild = discord.utils.get(client.guilds, name=GUILD)
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.content == "sindri": 
#         await message.channel.send("er en faggot ez")

#     if message.content == "/help":
#         await message.channel.send("nej")

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(f'Hej {member.name}, Velkommen til serveren!')

# client.run(TOKEN)

bot = commands.Bot(command_prefix="-")

@bot.command()
async def posture(ctx):
    if ctx.author.voice:
        await ctx.reply(f"Joining {ctx.author.name}'s channel ☜(ﾟヮﾟ☜)")
        vc = await ctx.author.voice.channel.connect()

        source = FFmpegPCMAudio(executable="C:/ffmpeg/ffmpeg.exe", source='sound.mp3')

        def set_interval():
            vc.play(source, after=None)
            Timer(10.0, set_interval).start()
            
        Timer(10.0, set_interval).start()
    else:
        await ctx.reply("You must be in a voice channel.")


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        Timer.cancel()
    else:
        await ctx.send("I am not in a voice channel.")

bot.run(TOKEN)