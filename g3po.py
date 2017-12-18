import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix = bot_prefix)
load_dotenv(find_dotenv(), override=True)

@client.event
async def on_ready():
    print("Booting up...")
    print("Bot online.")
    print("Name: ()" + client.user.name)
    print("ID: ()" + client.user.id)
    await client.send_message(client.get_channel('371880461900840975'), "G3-PO is online.")

def speach_commands(command: str, message: str):

    eval("@client.command(pass_context=True) \n async def " + command + "(ctx): \nawait client.say("+ message +")")

speach_commands("test", "it works your welcome")

@client.command(pass_context=True)
async def rules(ctx):
    await client.say("Do we really need to say this? Don't be a jerk if you don't want to be kicked. Otherwise, have fun, and may your own goals ever be better than your normal shots.")

@client.command(pass_context=True)
async def join(ctx):
    await client.say("If you're here you are probably apart of G3 already... If not, feel free to try out and play with us. If we like you, we will (in a totally objective manner) have you join the team!")

@client.command(pass_context=True)
async def youtube(ctx):
    await client.say("https://www.youtube.com/channel/UCBawivEhKKorAVE1s7wclLA")

@client.command(pass_context=True)
async def members(ctx):
    await client.say("SirOxion: Founder and owner")
    await client.say("Coolio: Co-Founder and Co-owner")
    await client.say("GummyJbear: An original G3 member")
    await client.say("Hockeykid33: A new aspiring G3 member")
    await client.say("Kronoby: A G3 member")
    await client.say("Syna: Graphic designer, and member")

@client.command(pass_context=True)
async def hi(ctx):
    await client.say("Hey... What do you want? I'm here to answer queries and rules, not be your convo partner")

client.run(os.environ.get("BOT_KEY"))