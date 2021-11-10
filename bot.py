
import os
import time

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
    ctx.voice_client.play(source, after=lambda e: bot.loop.create_task(play_source(ctx)))
    time.sleep(3)

@bot.command()
async def posture(ctx):
    if ctx.author.voice and not ctx.voice_client:
        await ctx.reply(f"Joining {ctx.author.name}'s channel ☜(ﾟヮﾟ☜)")
        await ctx.author.voice.channel.connect()

        bot.loop.create_task(play_source(ctx))
        time.sleep(3)

    else:
        await ctx.reply("You must be in a voice channel.")


# @bot.command()
# async def leave(ctx):
#     await ctx.voice_client.disconnect()
#     await ctx.reply("I'm out, cya!")
    # if ctx.voice_client:
        # This line throws error, why?
        # PLACEHOLDER
    # else:
        # await ctx.send("I am not in a voice channel.")

bot.run(TOKEN)