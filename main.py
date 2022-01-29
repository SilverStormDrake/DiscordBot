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


@bot.slash_command(guild_ids = token_info.__testserverID)
async def getchannelid(ctx):
    await ctx.send(ctx.channel.id)


@bot.slash_command(guild_ids = token_info.__testserverID)
async def getmessageid(ctx):
    await ctx.send(ctx.message.id)

@bot.slash_command(guild_ids = token_info.__testserverID)
async def getguilds(ctx):
    for a in bot.guilds:
        print(a)
    print(f"Total: {len(bot.guilds)}")
    await ctx.send(f"In {len(bot.guilds)} Servers")


@bot.slash_command(guild_ids = token_info.__testserverID) #For some reason slash_command doesnt work in small servers
async def ping(ctx):
    await ctx.send("Pong")

@bot.slash_command(guild_ids = token_info.__testserverID)
async def getguildid(ctx):
    await ctx.send(ctx.guild.id)



bot.run(token_info.__token)