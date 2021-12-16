import os
import discord
import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from keep_alive import keep_alive
treeimg = open('trees.txt', 'r')
treeinimgs = treeimg.readlines()
snowimg = open('snow.txt', 'r')
snowinimgs = snowimg.readlines()
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
my_secret = os.environ['token']
client = commands.Bot(command_prefix=("w?"),help_command=None)
slash = SlashCommand(client, sync_commands=True)
guild_ids = [889924479046778900]


@client.event
async def on_ready():
  print("ready")

@slash.slash(name="tree",
             description="Your Tree")
async def tree(ctx):
    finalimg = random.choice(treeinimgs)
    embed = discord.Embed(title='Your Tree')
    embed.set_image(url=finalimg)
    await ctx.send(embed=embed)

@client.command()
async def _tree(ctx):
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

@slash.slash(name="snow",
             description="Your Snow")
async def _snow(ctx):
    finalimg = random.choice(snowinimgs)
    embed = discord.Embed(title='Your Snow')
    embed.set_image(url=finalimg)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed=discord.Embed(title="HELP")
  embed.add_field(name="w?tree",value="Sends you an random image of an tree")
  embed.add_field(name="ww!snow",value="Sends you an random image of snow.",inline=False)
  await ctx.send(embed=embed)

@slash.slash(name="help",
             description="Commands")
async def _help(ctx):
    embed=discord.Embed(title="HELP")
    embed.add_field(name="/tree",value="Sends you an random image of an tree")
    embed.add_field(name="/snow",value="Sends you an random image of snow.",inline=False)
    await ctx.send(embed=embed)

keep_alive()
client.run(my_secret)
