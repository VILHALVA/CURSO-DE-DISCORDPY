# ADICIONAR CARGOS POR REAÇÕES
Adicionar cargos por reações é uma prática comum em servidores do Discord para permitir que os usuários escolham seus interesses ou categorias de forma interativa. Vamos explorar como implementar isso usando Discord.py, onde os usuários podem adicionar ou remover cargos ao reagir a uma mensagem específica.

## 1. Configuração Inicial
Certifique-se de que você tenha o Discord.py instalado e que tenha criado um bot no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).

## 2. Criar uma Mensagem de Configuração
Primeiro, crie uma mensagem no canal desejado que os usuários usarão para adicionar ou remover cargos por reações. Esta mensagem deve conter emojis que representem os cargos que os usuários podem escolher.

## 3. Implementar o Código
Aqui está um exemplo básico de como você pode implementar a funcionalidade de adicionar cargos por reações usando Discord.py:

```python
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
```

## Explicação do Código
- **role_emojis**: Um dicionário que mapeia emojis aos IDs dos cargos no Discord. Cada chave é um emoji e o valor é o ID do cargo correspondente.
- **on_ready()**: Evento que envia a mensagem de configuração e adiciona as reações aos emojis definidos no dicionário `role_emojis` quando o bot está pronto.
- **on_raw_reaction_add()**: Evento acionado quando um usuário adiciona uma reação a uma mensagem. O bot verifica se a reação foi feita na mensagem de configuração e, se sim, adiciona o cargo correspondente ao usuário.
- **on_raw_reaction_remove()**: Evento acionado quando um usuário remove uma reação de uma mensagem. O bot verifica se a reação foi removida da mensagem de configuração e, se sim, remove o cargo correspondente do usuário.

## Observações Importantes
- Certifique-se de substituir `YOUR_BOT_TOKEN` pelo token real do seu bot Discord.
- Substitua os valores de `channel_id` pelos IDs reais do canal e dos cargos que você está usando.
- Este código é um exemplo básico e pode ser expandido para lidar com mais emojis e cargos, ou para adicionar verificação de permissões e tratamento de erros mais robustos.

Ao executar este bot, os usuários poderão reagir à mensagem de configuração com emojis designados e receberão automaticamente os cargos correspondentes no servidor Discord.