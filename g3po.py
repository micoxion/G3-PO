import discord
from urllib import request
from bs4 import BeautifulSoup
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

Client = discord.Client()
bot_prefix = "!"
g3po = commands.Bot(command_prefix = bot_prefix)
load_dotenv(find_dotenv(), override=True)

bot_dev = '395402947292561410'
g3_team = '371880461900840975'

super_user = '331634391790911488'

im_active = True

@g3po.event
async def on_ready():
    print("Booting up...")
    print("Bot online.")
    print("Name: ()" + g3po.user.name)
    print("ID: ()" + g3po.user.id)
    await g3po.send_message(g3po.get_channel(g3_team), "Hello, I am G3-PO, rocket league cyborg relations. How may I help you?")
    #await g3po.send_message(g3po.get_channel(bot_dev), "Hello, I am G3-PO, rocket league cyborg relations. How may I help you?")

@g3po.command(pass_context=True)
async def syna_n_g3(ctx):
    await g3po.say("https://media.discordapp.net/attachments/371880461900840975/396160765297426452/Syna__G3.png?width=1248&height=702")

@g3po.command(pass_context=True)
async def toggle_im(ctx):
    global im_active
    print(im_active)
    if (ctx.message.author.id == super_user):
        im_active = not im_active

@g3po.command(pass_context=True)
async def gamer_spam(ctx):
    await g3po.say("The \"Gamer\" who's spamming Coolio -- Seen Live Kappa\nhttps://giphy.com/gifs/break-free-HTZVeK0esRjyw ")

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
    await g3po.say("Coolio (a.k.a Coolaid): G3 Co-Founder and Co-owner")
    await g3po.say("GummyJbear: G3 Founder (not active much)")
    await g3po.say("Hockeykid33: G3 member")
    await g3po.say("DubsOnIce: G3 member")
    await g3po.say("Syna: Graphic designer, and member")

@g3po.command(pass_context=True)
async def hi(ctx):
    await g3po.say("Hey... What do you want? I'm here to answer queries and rules, not be your convo partner")

@g3po.command(pass_context=True)
async def commands(ctx):
    await g3po.say("!tourney: in development, will give the ability to recieve faceit tourney info from me.\n" +
                   "Based on either 1s, 2s, or 3s\n\n!meow: requested by syna himself and comming soon\n\n" +
                   "!rules: the rules... what did you expect?\n\n!join: a little info on our new member procedure\n\n" +
                   "!youtube: just our youtube link... GO CHECK IT OUT!\n\n" +
                   "!members: a list of official G3 members barring subs")

@g3po.event
async def on_message(message):
    if message.author != g3po.user:
        if im_active:
            if "i\'m" in message.content.lower():
                if len(message.content[message.content.lower().find("i\'m") + 3:]) > 0:
                    await g3po.send_message(message.channel, "Hi " +
                                            message.content[message.content.lower().find("i\'m") + 4: len(message.content)] +
                                            "! I'm G3-PO")
                else:
                    await g3po.send_message(message.channel, message.author.name + ", you're what?!")

    await g3po.process_commands(message)

g3po.run(os.environ.get("BOT_KEY"))