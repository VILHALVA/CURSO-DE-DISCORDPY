import discord
from discord.ext import commands

# Insira o Token do seu bot aqui
TOKEN = 'YOUR_BOT_TOKEN'

# Define os intents que seu bot vai usar
intents = discord.Intents.default()

# Cria o objeto do bot com os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)

# Canal de boas-vindas (substitua pelo ID do seu canal)
welcome_channel_id = 1234567890

# Mensagem de boas-vindas
welcome_message = """
Bem-vindo ao nosso servidor, {member}! Esperamos que você se divirta por aqui!
"""

# Evento que dispara quando um novo membro se junta ao servidor
@bot.event
async def on_member_join(member):
    # Encontra o canal de boas-vindas
    channel = bot.get_channel(welcome_channel_id)
    if channel:
        # Formata a mensagem de boas-vindas com o nome do membro
        formatted_message = welcome_message.format(member=member.mention)
        # Envia a mensagem de boas-vindas no canal específico
        await channel.send(formatted_message)

# Evento que dispara quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Inicia o bot
bot.run(TOKEN)
