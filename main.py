import discord
import token_info
import logging
from discord.ext import commands

''' Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
'''

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')


@bot.slash_command(guild_ids = token_info.__testserverID, description = "Returns the channel ID")
async def getchannelid(ctx):
    await ctx.send(ctx.channel.id)


@bot.slash_command(guild_ids = token_info.__testserverID, description = "Returns the message ID of the command")
async def getmessageid(ctx):
    await ctx.send(ctx.message.id)

@bot.slash_command(guild_ids = token_info.__testserverID, description = "Return the amount of guilds that the bot is logged in")
async def getguilds(ctx):
    for a in bot.guilds:
        print(a)
    print(f"Total: {len(bot.guilds)}")
    await ctx.send(f"In {len(bot.guilds)} Servers")


@bot.slash_command(guild_ids = token_info.__testserverID, description = "Returns pong") # For some reason slash_command doesnt work in small servers
async def ping(ctx):
    await ctx.send("Pong")

@bot.slash_command(guild_ids = token_info.__testserverID, description = "Return the server ID")
async def getguildid(ctx):
    await ctx.send(ctx.guild.id)

@bot.slash_command(guild_ids = token_info.__testserverID, description = "Returns the message passed as parameter") # Thats cool
async def echo(ctx, msg):
    await ctx.send(msg)

@bot.slash_command(guild_ids = token_info.__testserverID, description = "Simple Math operations: sum(+), subtract(-), divide(/) and multiply(*). Separate all terms by spaces")
async def math(ctx, msg):
    x = msg.split(' ')
    num1 = int(x[0])
    num2 = int(x[2])

    if x[1] == '+' :
        result:int = num1 + num2
    elif x[1] == '-':
        result:int = num1 - num2
    elif x[1] == '*':
        result:int = num1 * num2
    elif x[1] == '/':
        result:float = num1 / num2

    await ctx.send(result)

#TODO /play command
@bot.slash_command(guild_ids = token_info.__testserverID, description = "Play a music passed by a youtube link")
async def play(ctx, link):
    discord.VoiceChannel.connect()

bot.run(token_info.__token)