import discord
import datetime
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

Client = discord.Client()
bot_prefix = "!"
g3po = commands.Bot(command_prefix = bot_prefix)
load_dotenv(find_dotenv(), override=True)

@g3po.event
async def on_ready():
    print("Booting up...")
    print("Bot online.")
    print("Name: ()" + g3po.user.name)
    print("ID: ()" + g3po.user.id)
    await g3po.send_message(g3po.get_channel('371880461900840975'), "Hello, I am G3-PO, human rocket league relations. How may I help you?")

@g3po.command(pass_context=True)
async def rules(ctx):
    await g3po.say("Do we really need to say this? Don't be a jerk if you don't want to be kicked. Otherwise, have fun, and may your own goals ever be better than your normal shots.")

@g3po.command(pass_context=True)
async def join(ctx):
    await g3po.say("If you're here you are probably apart of G3 already... If not, feel free to try out and play with us. If we like you, we will (in a totally objective manner) have you join the team!")

@g3po.command(pass_context=True)
async def youtube(ctx):
    await g3po.say("https://www.youtube.com/channel/UCBawivEhKKorAVE1s7wclLA")

@g3po.command(pass_context=True)
async def members(ctx):
    await g3po.say("SirOxion: Founder and owner")
    await g3po.say("Coolio: Co-Founder and Co-owner")
    await g3po.say("GummyJbear: An original G3 member")
    await g3po.say("Hockeykid33: A new aspiring G3 member")
    await g3po.say("Kronoby: A G3 member")
    await g3po.say("Syna: Graphic designer, and member")

@g3po.command(pass_context=True)
async def goodmorning(ctx):
    cur_time = datetime.datetime.now()
    if cur_time <= datetime.datetime(cur_time.year, cur_time.month, cur_time.day, 12):
        await g3po.say("Good morning")
    else:
        await g3po.say("Someones a little too tired today")

@g3po.command(pass_context=True)
async def hi(ctx):
    await g3po.say("Hey... What do you want? I'm here to answer queries and rules, not be your convo partner")

g3po.run(os.environ.get("BOT_KEY"))