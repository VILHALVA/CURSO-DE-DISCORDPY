# WELCOME - BEM-VINDO
Para criar um sistema de boas-vindas (welcome) eficaz em um servidor do Discord usando Discord.py, você pode implementar um bot que envia uma mensagem de boas-vindas personalizada sempre que um novo membro se junta ao servidor. Vamos passar por como configurar isso:

## 1. Configuração Inicial
Certifique-se de que você tenha o Discord.py instalado e que tenha criado um bot no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).

## 2. Implementação do Código
Aqui está um exemplo básico de como você pode criar um sistema de boas-vindas com Discord.py:

```python
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
```

## Explicação do Código
- **welcome_channel_id**: Substitua `1234567890` pelo ID do canal onde você deseja enviar a mensagem de boas-vindas.
- **welcome_message**: Mensagem de boas-vindas que será enviada quando um novo membro se juntar ao servidor. `{member}` é um espaço reservado que será substituído pelo nome mencionável do novo membro.
- **on_member_join(member)**: Evento que é disparado sempre que um novo membro se junta ao servidor. Ele encontra o canal de boas-vindas especificado e envia a mensagem formatada para dar as boas-vindas ao novo membro.
- **on_ready()**: Evento que é disparado quando o bot está pronto e conectado ao Discord.

## Observações Importantes
- Certifique-se de substituir `YOUR_BOT_TOKEN` pelo token real do seu bot Discord.
- Adapte `welcome_channel_id` para o ID real do canal onde você deseja enviar as mensagens de boas-vindas.
- Personalize `welcome_message` conforme necessário para se adequar ao estilo e tom do seu servidor.

Ao executar este bot, toda vez que um novo membro se juntar ao servidor, ele receberá automaticamente uma mensagem de boas-vindas no canal configurado. Isso cria uma experiência acolhedora para novos membros e pode ajudar a integrá-los à comunidade do seu servidor Discord.