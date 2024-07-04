# PRIMEIRO COMANDO
Vamos criar um exemplo simples de um primeiro comando assíncrono utilizando Python e Discord.py. Neste caso, vamos criar um comando `!hello` que fará o bot responder com uma mensagem de saudação.

Certifique-se de que você já tenha instalado o Discord.py conforme as instruções anteriores.

1. **Código Python**

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

# Comando assíncrono de exemplo
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

# Inicia o bot
bot.run(TOKEN)
```

## Explicação do Código
- **Importações**: Importamos as bibliotecas necessárias do Discord.py.
- **TOKEN**: Substitua `'YOUR_BOT_TOKEN'` pelo token do seu bot Discord. Este token é obtido no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).
- **intents**: Definimos os intents necessários para o bot funcionar corretamente. No exemplo, usamos `discord.Intents.default()` para obter os intents padrão.
- **bot**: Criamos o objeto do bot utilizando `commands.Bot`, especificando o prefixo de comando (`command_prefix='!'`) e os intents.
- **@bot.event on_ready()**: Um evento assíncrono que é disparado quando o bot está pronto e conectado ao Discord.
- **@bot.command() hello()**: Um comando assíncrono `hello` que pode ser invocado pelo prefixo `!hello`. Ele usa `ctx` (Contexto) para enviar uma mensagem de saudação mencionando o autor da mensagem.
- **bot.run(TOKEN)**: Inicia o bot, conectando-o ao Discord usando o token especificado.

## Como Usar
1. **Execute o Bot**:
   - Salve o código acima em um arquivo Python (por exemplo, `bot.py`).
   - Execute o arquivo `bot.py` no terminal usando o comando `python bot.py`.

2. **Teste o Comando**:
   - No servidor do Discord onde seu bot está adicionado, digite `!hello` em qualquer canal de texto.
   - O bot deverá responder com uma mensagem de saudação.

Este é um exemplo básico para começar a entender como criar comandos assíncronos usando Discord.py. Você pode expandir este exemplo adicionando mais comandos e explorando outras funcionalidades da biblioteca conforme necessário.