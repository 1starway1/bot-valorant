import os
import discord
import random
import asyncio
import json
import functools
import itertools
import math
from discord import Option
from random import randrange    
from discord.ext import commands,tasks
from discord import FFmpegPCMAudio




token = '***'

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='-', intents=intents)

guns = ['Classic', 'Frenzy', 'Shorty', 'Ghost', 'Sherif', 'Stinger', 'Bucky', 'Judge', 'Marshal', 'Operator', 'Ares', 'Odin', 'Spectre', 'Phantom', 'Vandal', 'Bulldog', 'Guardian', 'Knife']
agents = ['Астра', 'Бримстоун', 'Сайфер', 'Рейна', 'Сейдж', 'Рейз', 'Омен', 'Гекко', 'Чембер', 'Джетт', 'Йору', 'Вайпер', 'Брич', 'Неон', 'Скай', 'Феникс', 'КиллДжой', 'Харбор', 'Фейд', 'Сова', 'Kay/O']
three_plants = ['A', 'B', 'C']
two_plants = ['A', 'B']


@bot.slash_command(name='pick', description='Выбирает случайного героя')
async def pick(ctx):
    await ctx.respond(f'**Сегодня ты играешь на:** `{random.choice(agents)}`')        

@bot.slash_command(name='roll', description='Выдает рандомное число')
async def __roll(ctx):
    await ctx.respond(f'**Вам выпало число:** `{random.randint(1, 100)}`')

@bot.slash_command(name = 'gun', description = 'Выбирает случайное оружие, с которым вы должны будете играть следующий раунд/матч')
async def __gun(ctx):
    await ctx.respond(f'**В следующем раунде вы будете играть с:** `{random.choice(guns)}`')

@bot.slash_command(name = 'defender', description = 'Выбирает, на каком вы плент стоите в этом раунде')
async def __defender(ctx,
    choice: Option(str, description="Выберите карту, на который вы играете", required=True,  choices=['Haven','IceBox','Bind','Breeze','Pearl','Fracture','Split', 'Ascent', 'Lotus'])):
    if choice == 'Haven':
        await ctx.respond(f'**Карта: `Haven`\nРекомендую встать на плент:** `{random.choice(three_plants)}`')
    if choice == 'IceBox':
        await ctx.respond(f'**Карта: `IceBox`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Bind':
        await ctx.respond(f'**Карта: `Bind`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Breeze':
        await ctx.respond(f'**Карта: `Breeze`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Pearl':
        await ctx.respond(f'**Карта: `Pearl`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Fracture':
        await ctx.respond(f'**Карта: `Fracture`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Split':
        await ctx.respond(f'**Карта: `Split`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Ascent':
        await ctx.respond(f'**Карта: `Ascent`\nРекомендую встать на плент:** `{random.choice(two_plants)}`')
    if choice == 'Lotus':
        await ctx.respond(f'**Карта: `Lotus`\nРекомендую встать на плент:** `{random.choice(three_plants)}`')

@bot.slash_command(name = 'attack', description = 'Выбирает, на какой плент лучше зайти')
async def __defender(ctx,
    choice: Option(str, description="Выберите карту, на который вы играете", required=True,  choices=['Haven','IceBox','Bind','Breeze','Pearl','Fracture','Split', 'Ascent', 'Lotus'])):
    if choice == 'Haven':
        await ctx.respond(f'**Карта: `Haven`\nРекомендую зайти на плент:** `{random.choice(three_plants)}`')
    if choice == 'IceBox':
        await ctx.respond(f'**Карта: `IceBox`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Bind':
        await ctx.respond(f'**Карта: `Bind`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Breeze':
        await ctx.respond(f'**Карта: `Breeze`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Pearl':
        await ctx.respond(f'**Карта: `Pearl`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Fracture':
        await ctx.respond(f'**Карта: `Fracture`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Split':
        await ctx.respond(f'**Карта: `Split`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Ascent':
        await ctx.respond(f'**Карта: `Ascent`\nРекомендую зайти на плент:** `{random.choice(two_plants)}`')
    if choice == 'Lotus':
        await ctx.respond(f'**Карта: `Lotus`\nРекомендую зайти на плент:** `{random.choice(three_plants)}`')

# @bot.slash_command(name = 'buy', description = 'Выбирает оптимальный закуп на раунд.')
# async def __buy(ctx,
#     number: Option(int, description="Количество кредиков(0-9000)", required=True, min_value=0, max_value=9000),
#     choice: Option(str, description="Выберите героя", required=True, choices=['Астра', 'Бримстоун', 'Сайфер', 'Рейна', 'Сейдж', 'Рейз', 'Омен', 'Гекко', 'Чембер', 'Джетт', 'Йору', 'Вайпер', 'Брич', 'Неон', 'Скай', 'Феникс', 'КиллДжой', 'Харбор', 'Фейд', 'Сова', 'Kay/O'])):
#     if number <= 2000 and choice == 'Астра':
#         await ctx.respond(f'Сделайте эко, купив {random.randint(1,3)} ')
#     if number <= 2000 and choice == 'Бримстоун':
#         await ctx.respond(f'**Сделайте эко, купив `{random.randint(2,3)} смока`**')

bot.run(token)
