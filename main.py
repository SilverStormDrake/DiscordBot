import discord
import token_info
import logging
from discord.ext import commands


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = discord.Bot()

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')
    print('\n')


@bot.command()
async def getchannelid(ctx):
    await ctx.trigger_typing()
    await ctx.send(ctx.channel.id)


@bot.command()
async def cool(ctx):
    await ctx.delete


bot.run(token_info.__token)