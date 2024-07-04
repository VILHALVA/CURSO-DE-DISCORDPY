import discord
from discord.ext import commands

# Insira o Token do seu bot aqui
TOKEN = 'YOUR_BOT_TOKEN'

# Define os intents que seu bot vai usar
intents = discord.Intents.default()

# Cria o objeto do bot com os intents definidos
bot = commands.Bot(command_prefix='!', intents=intents)

# ID do canal onde a mensagem de configuração será enviada
channel_id = 1234567890  # Substitua pelo ID do seu canal

# Emojis correspondentes aos cargos que os usuários podem escolher
role_emojis = {
    '🔵': 123456789012345678,  # Emoji e ID do cargo
    '🔴': 123456789012345678,
    '🟢': 123456789012345678,
    # Adicione mais emojis e IDs de cargos conforme necessário
}

# Evento que dispara quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    channel = bot.get_channel(channel_id)
    if channel:
        message = await channel.send("Reaja com um emoji para obter um cargo:")
        for emoji in role_emojis:
            await message.add_reaction(emoji)

# Evento que dispara quando uma reação é adicionada a uma mensagem
@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    if channel.id == channel_id:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                emoji = str(payload.emoji)
                if emoji in role_emojis:
                    role = guild.get_role(role_emojis[emoji])
                    if role:
                        await member.add_roles(role)
                        await channel.send(f'{member.mention}, cargo {role.name} adicionado!')

# Evento que dispara quando uma reação é removida de uma mensagem
@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(payload.channel_id)
    if channel.id == channel_id:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                emoji = str(payload.emoji)
                if emoji in role_emojis:
                    role = guild.get_role(role_emojis[emoji])
                    if role:
                        await member.remove_roles(role)
                        await channel.send(f'{member.mention}, cargo {role.name} removido.')

# Inicia o bot
bot.run(TOKEN)
