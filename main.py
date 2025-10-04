import os
import random
import discord
from discord.ext import commands

PLAYERS = []

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="c.", intents=intents)

@bot.event
async def on_ready():
  print("{0.user}".format(bot), 'is online')



@bot.command()
async def join(ctx):
  global PLAYERS
  user = ctx.message.author
  if user not in PLAYERS:
    PLAYERS.append(user)
    role = discord.utils.get(user.guild.roles, name="Researcher")
    await user.add_roles(role)
    await ctx.channel.send("You have joined the game, there are currently " + str(len(PLAYERS)) + " player(s)")

@bot.command()
async def leave(ctx):
  global PLAYERS
  user = ctx.message.author
  PLAYERS.remove(user)
  role = discord.utils.get(user.guild.roles, name="Researcher")
  await user.remove_roles(role)
  await ctx.channel.send("You have left the game")

@bot.command()
async def clear(ctx):
  global PLAYERS
  all_members = ctx.guild.members
  for member in all_members:
    role = discord.utils.get(member.guild.roles, name="Researcher")
    if role in member.roles:
      await member.remove_roles(role)
  PLAYERS = []
  await ctx.channel.send(
    "The game has been reset, use c.join to join the game")

@bot.command()
async def start(ctx):
  global PLAYERS
  if len(PLAYERS) >= 2:
    alien1 = random.randint(1, len(PLAYERS))
    alien2 = random.randint(1, len(PLAYERS))
    while alien1 == alien2:
      alien2 = random.randint(1, len(PLAYERS))
    for i in range(len(PLAYERS)):
      if i == alien1 - 1 or i == alien2 - 1:
        message = 'https://cdn.discordapp.com/attachments/749536300712984687/1079662301063426068/Alien.png'
      else:
        message = 'https://cdn.discordapp.com/attachments/749536300712984687/1079662214182600774/Human.png'
      await PLAYERS[i].send(message)
  else:
    await ctx.channel.send("Not enough players")

@bot.command()
async def roll(ctx, member1: discord.Member = None, member2: discord.Member = None, member3: discord.Member = None, member4: discord.Member = None, member5: discord.Member = None, member6: discord.Member = None):
  global PLAYERS
  user = ctx.message.author
  r = random.random()
  message = ''
  if r < (1/6): # 1/6
    message = 'https://cdn.discordapp.com/attachments/749536300712984687/1079079545749131324/Syringe_Dice.png'
  elif r < (1/2): # 1/3
    message = 'https://cdn.discordapp.com/attachments/749536300712984687/1079079540476883035/Part_Dice.png'
  else: # 1/2
    message = 'https://cdn.discordapp.com/attachments/749536300712984687/1079078190938599474/Alien_Dice.png'
  await user.send(message)
  if member1 != None:
    await member1.send(message)
  if member2 != None:
    await member2.send(message)
  if member3 != None:
    await member3.send(message)
  if member4 != None:
    await member4.send(message)
  if member5 != None:
    await member5.send(message)
  if member6 != None:
    await member6.send(message)


bot.run(os.environ['BOT_TOKEN'])
