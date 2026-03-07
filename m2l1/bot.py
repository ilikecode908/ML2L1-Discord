import discord
from discord.ext import commands
from config import TOKEN
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Signed as this.')

@bot.command()
async def meme1(ctx):
    with open('images/meme1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meme2(ctx):
    with open('images/meme2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meme3(ctx):
    with open('images/meme3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def random_meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mymeme(ctx):
    with open('images/mymeme.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def life(ctx):
    with open('images/life.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    with open('images/animals.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def snackmeme(ctx):
    with open('images/snackmeme.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(TOKEN)