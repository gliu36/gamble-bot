import discord
from discord.ext import commands
import json

token = 'from config.json'
with open('config.json') as f:
    token = json.load(f)['token']

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('hi im on')

@client.event
async def on_message(msg):
    user = msg.author
    m = msg.content
    print(f"{user} said {m}")

@client.command()
async def ping(ctx):
    await ctx.send('owo')

client.run(token)