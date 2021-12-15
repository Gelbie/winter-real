import os
import discord
import random
treeimg = open('trees.txt', 'r')
treeinimgs = treeimg.readlines()
snowimg = open('snow.txt', 'r')
snowinimgs = snowimg.readlines()
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
my_secret = os.environ['token']
client = commands.Bot(command_prefix=("!"))
slash = SlashCommand(client)


@client.command()
async def tree(ctx):
  finalimg= random.choice(treeinimgs)
  embed= discord.Embed(title="Your Tree")
  embed.set_image(url=finalimg)
  await ctx.send(embed=embed)

@client.command()
async def snow(ctx):
  finalimg= random.choice(snowinimgs)
  embed= discord.Embed(title="Your Snow")
  embed.set_image(url=finalimg)
  await ctx.send(embed=embed)
client.run(my_secret)
