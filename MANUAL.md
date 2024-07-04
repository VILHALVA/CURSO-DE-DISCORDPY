# MANUAL
## INSTALAÇÃO:
1. **Instalar Python**:
   Primeiro, você precisa ter o Python instalado na sua máquina. Baixe a versão mais recente do [site oficial do Python](https://www.python.org/downloads/) e siga as instruções de instalação.

2. **Instalar discord.py**:
   Use o pip para instalar a biblioteca discord.py. Abra o terminal (ou prompt de comando) e execute:
   ```bash
   pip install discord.py
   ```

### CONFIGURAÇÃO:
1. **Criar um Bot no Discord**:
   - Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).
   - Clique em "New Application" e dê um nome ao seu bot.
   - No menu à esquerda, vá para "Bot" e clique em "Add Bot".
   - Clique em "Copy" para copiar o Token do Bot. Você precisará dele para conectar seu bot ao servidor.

2. **Adicionar o Bot a um Servidor**:
   - No Portal de Desenvolvedores do Discord, vá para "OAuth2" e depois para "URL Generator".
   - Em "Scopes", selecione "bot".
   - Em "Bot Permissions", selecione as permissões necessárias (por exemplo, enviar mensagens).
   - Copie o URL gerado e cole no seu navegador para adicionar o bot ao seu servidor.

## PRIMEIRO BOT:
1. **Crie um Arquivo Python**:
   - Crie um novo arquivo Python no seu editor de código favorito (por exemplo, `bot.py`).

2. **Escreva o Código do Bot**:
   - Cole o seguinte código no arquivo `bot.py`:
   ```python
   import discord
   from discord.ext import commands

   # Insira o Token do seu bot aqui
   TOKEN = 'YOUR_BOT_TOKEN'

   # Define os intents que seu bot vai usar
   intents = discord.Intents.default()
   intents.messages = True  # Permitir leitura de mensagens

   # Cria o objeto do bot com os intents definidos
   bot = commands.Bot(command_prefix='!', intents=intents)

   # Evento que dispara quando o bot está pronto
   @bot.event
   async def on_ready():
      print(f'Bot conectado como {bot.user}')

   # Comando de exemplo
   @bot.command()
   async def ping(ctx):
      await ctx.send('Pong!')

   # Inicia o bot
   bot.run(TOKEN)
   ```

3. **Execute o Bot**:
   - No terminal (ou prompt de comando), navegue até o diretório onde seu arquivo `bot.py` está localizado e execute:
   ```bash
   python bot.py
   ```

4. **Teste o Bot**:
   - Vá para o servidor do Discord onde você adicionou o bot e digite `!ping`. O bot deve responder com `Pong!`.

Pronto! Agora você tem um bot básico funcionando com discord.py. Você pode expandir e adicionar mais comandos e eventos conforme sua necessidade.