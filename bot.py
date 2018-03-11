# GAMEOVER-bot
discord bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime

bot = commands.Bot(command_prefix="$")
d = datetime.date.today()

@bot.event
async def on_ready():
    print("bot started")
    print("name = " + bot.user.name)
    print("id = " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='version 1.1'))

@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="PONG", description=":ping_pong:", color=0xf0546a)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Users info.", color=0xfff200)
    embed.add_field(name="NAME", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="STATUS", value=user.status, inline=True)
    embed.add_field(name="HIGHEST ROLE", value=user.top_role)
    embed.add_field(name="JOINED", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Servers info.", color=0xf0546a)
    embed.set_author(name="GAME OVER")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Was created:", value=ctx.message.server.created_at)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def date(ctx):
    embed = discord.Embed(name="Today's date", color=0x7fffd4)
    embed.add_field(name="Today's date", value= d)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def game(ctx, user: discord.Member):
    embed = discord.Embed(name="Game", color=0xf0546a)
    embed.add_field(name="Currently playing: ", value=user.game.name)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def flip(ctx):
    flip = random.choice(["Head", "Tail"])
    embed = discord.Embed(name="FLIP", color=0x2669ff)
    embed.add_field(name="Coin:", value= flip)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def q(ctx, *, question: str):
    ball = random.choice(["yes", "no"])
    embed = discord.Embed(name="FLIP", color=0xf0546a)
    embed.set_author(name="Question:")
    embed.add_field(name= question, value= ball)
    await bot.say(embed=embed)


@bot.command()
async def echo(*, message: str):
    await bot.say(message)   






bot.run("NDIyMDAyMTY5NDIwNTc4ODE3.DYVbsw.Ys1omEcl5RQfERKHZ8O3qAzX9JE")
