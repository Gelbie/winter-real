import os
import discord
import music
import random
import youtube_dl
from keep_alive import keep_alive
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
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

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
  print("ready")

@slash.slash(name="tree",
             description="Your Tree", guild_ids=guild_ids)
async def tree(ctx):
    finalimg = random.choice(treeinimgs)
    embed = discord.Embed(title='Your Tree')
    embed.set_image(url=finalimg)
    await ctx.send(embed=embed)

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

@slash.slash(name="snow",
             description="Your Snow", guild_ids=guild_ids)
async def snow(ctx):
    finalimg = random.choice(snowinimgs)
    embed = discord.Embed(title='Your Snow')
    embed.set_image(url=finalimg)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  embed=discord.Embed(title="HELP")
  embed.add_field(name="w?tree",value="Sends you an random image of an tree")
  embed.add_field(name="w?snow",value="Sends you an random image of snow.",inline=False)
  await ctx.send(embed=embed)

@slash.slash(name="help",
             description="Commands", guild_ids=guild_ids)
async def help(ctx):
    embed=discord.Embed(title="HELP")
    embed.add_field(name="w?tree",value="Sends you an random image of an tree")
    embed.add_field(name="w?snow",value="Sends you an random image of snow.",inline=False)
    await ctx.send(embed=embed)


keep_alive()
client.run(my_secret)
