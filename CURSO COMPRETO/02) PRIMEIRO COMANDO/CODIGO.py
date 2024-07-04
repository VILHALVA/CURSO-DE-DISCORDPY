import discord
from discord.ext import commands

# Insira o Token do seu bot aqui
TOKEN = 'YOUR_BOT_TOKEN'

# Define os intents que seu bot vai usar
intents = discord.Intents.default()

# Cria o objeto do bot com os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento que dispara quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando assíncrono de exemplo
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

# Inicia o bot
bot.run(TOKEN)
