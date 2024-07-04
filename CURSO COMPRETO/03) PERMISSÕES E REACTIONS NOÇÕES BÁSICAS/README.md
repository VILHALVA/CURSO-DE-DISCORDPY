# PERMISSÕES E REACTIONS NOÇÕES BÁSICAS
Vamos abordar as noções básicas sobre permissões e reações no Discord, que são fundamentais para entender como o Discord.py e outros bots interagem com esses recursos.

## Permissões no Discord
As permissões no Discord controlam o que os usuários podem fazer em um servidor ou canal específico. Elas são divididas em categorias como **Permissões de Texto**, **Permissões de Voz** e **Permissões Administrativas**. Alguns exemplos de permissões incluem:

- **Enviar Mensagens**: Permite que os usuários enviem mensagens em um canal.
- **Gerenciar Mensagens**: Permite que os usuários excluam, editem ou fixem mensagens.
- **Conectar-se**: Permite que os usuários se conectem a um canal de voz.
- **Administrador**: Concede acesso a todas as permissões em um servidor.

As permissões são configuradas pelos administradores do servidor no Discord através das configurações de papel (role) e canais.

## Reações no Discord
As reações permitem que os usuários interajam com mensagens adicionando emojis como reações. Cada mensagem pode ter várias reações, e cada reação é associada a um emoji específico. Algumas características das reações incluem:

- **Adicionar Reações**: Os usuários podem clicar em um emoji para adicioná-lo como reação a uma mensagem.
- **Remover Reações**: Os usuários podem remover suas próprias reações clicando no emoji novamente.
- **Reações Animadas**: Certos emojis animados também podem ser usados como reações.

## Uso de Reações e Permissões em Bots (Discord.py)
Ao programar um bot usando Discord.py, você pode controlar como o bot interage com reações e permissões:

- **Ler e Adicionar Reações**: Use o evento `on_reaction_add` para detectar quando um usuário adiciona uma reação a uma mensagem.
  
- **Verificar Permissões**: Utilize métodos como `has_permissions()` e `bot_has_permissions()` para verificar se o bot ou um usuário tem permissões específicas antes de realizar uma ação, como enviar uma mensagem ou moderar um canal.

## Exemplo Básico (Discord.py)
Aqui está um exemplo simples de como você pode detectar quando um usuário adiciona uma reação a uma mensagem usando Discord.py:

```python
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

# Evento que dispara quando uma reação é adicionada a uma mensagem
@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(f'{user.name} reagiu com {reaction.emoji}!')

# Inicia o bot
bot.run(TOKEN)
```

Neste exemplo, o evento `on_reaction_add` é acionado sempre que um usuário adiciona uma reação a uma mensagem. O bot então envia uma mensagem para o mesmo canal indicando qual usuário reagiu com qual emoji.

## Conclusão
Entender permissões e reações é crucial para o desenvolvimento de bots eficazes no Discord. Com Discord.py, você pode explorar esses conceitos mais a fundo e implementar funcionalidades avançadas, como moderação de reações, interações baseadas em permissões e muito mais.