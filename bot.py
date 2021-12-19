
import os
import asyncio

from discord.ext import commands
from discord import FFmpegPCMAudio, voice_client
from discord import Client;

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="-")
# client = Client();

async def play_source(ctx):
    # put below for local use -> executable="C:/ffmpeg/ffmpeg.exe"
    source = FFmpegPCMAudio(source='sound.mp3')

    await asyncio.sleep(900)
    ctx.voice_client.play(source, after=lambda e: bot.loop.create_task(play_source(ctx)))

@bot.command()
async def posture(ctx):
    if ctx.author.voice and not ctx.voice_client:
        await ctx.reply(f"Joining {ctx.author.name}'s channel ☜(ﾟヮﾟ☜)")
        await ctx.author.voice.channel.connect()
        greeting = FFmpegPCMAudio(source='greeting.mp3')
        ctx.voice_client.play(greeting)

        bot.loop.create_task(play_source(ctx))

    else:
        await ctx.reply("You must be in a voice channel.")

@bot.command()
async def suh(ctx):
    if ctx.voice_client:
        greeting = FFmpegPCMAudio(source='greeting.mp3')
        await ctx.voice_client.play(greeting)
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def boi(ctx):
    if ctx.voice_client:
        islandboy = FFmpegPCMAudio(source='islandboy.mp3')
        await ctx.voice_client.play(islandboy)
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def dude(ctx):
    if ctx.voice_client:
        await ctx.reply("suh")
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.reply("I'm out, cya!")
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def sus(ctx):
    if ctx.voice_client:
        amogus = FFmpegPCMAudio(source='amogus.mp3')
        await ctx.voice_client.play(amogus)
    else:
        await ctx.send("I am not in a voice channel.")

@bot.command()
async def bunda(ctx):
    if ctx.voice_client:
        fatbunda = FFmpegPCMAudio(source='fatbunda.mp3')
        await ctx.voice_client.play(fatbunda)
    else:
        await ctx.send("I am not in a voice channel.")

# async def check():
#     memberCount = len(client.voice_channel.members)
#     if memberCount == 1:
#         client.voice_client.disconnect()
#     await asyncio.sleep(60)
# client.loop.create_task(check())

bot.run(TOKEN)