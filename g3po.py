import discord
import datetime
import google
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
    await g3po.send_message(g3po.get_channel('371880461900840975'), "Hello, I am G3-PO, rocket league cyborg relations. How may I help you?")

@g3po.event
async def on_message(message):
    if message.author != g3po.user:
        if "i\'m" in message.content.lower():
            await g3po.send_message(g3po.get_channel('371880461900840975'), "Hi " +
                                    message.content[message.content.lower().find("\'m") + 3: len(message.content)] +
                                    "! I'm G3-PO")


@g3po.command(pass_context=True)
async def meow(ctx):
    await g3po.say("Coming soon!")

@g3po.command(pass_context=True)
async def rules(ctx):
    await g3po.say("Do we really need to say this? Don't be a jerk if you don't want to be kicked. Otherwise, have fun, and may your own goals ever be better than your normal shots.")

@g3po.command(pass_context=True)
async def join(ctx):
    await g3po.say("Once you hit Gold 3 or higher, you can request to join! \nWe'll play some games with you, and see how your... \'Synergy\' is :wink:")

@g3po.command(pass_context=True)
async def youtube(ctx):
    await g3po.say("https://www.youtube.com/channel/UCBawivEhKKorAVE1s7wclLA")

@g3po.command(pass_context=True)
async def members(ctx):
    await g3po.say("SirOxion: G3 Founder and owner")
    await g3po.say("Coolio: G3 Co-Founder and Co-owner")
    await g3po.say("GummyJbear: G3 Founder (not active much)")
    await g3po.say("Hockeykid33: G3 member")
    await g3po.say("DubsOnIce: G3 member")
    await g3po.say("Syna: Graphic designer, and member")

@g3po.command(pass_context=True)
async def hi(ctx):
    await g3po.say("Hey... What do you want? I'm here to answer queries and rules, not be your convo partner")

g3po.run(os.environ.get("BOT_KEY"))