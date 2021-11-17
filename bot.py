
import os
import asyncio

from discord.ext import commands
from discord import FFmpegPCMAudio

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="-")

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
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.reply("I'm out, cya!")
    else:
        await ctx.send("I am not in a voice channel.")

bot.run(TOKEN)