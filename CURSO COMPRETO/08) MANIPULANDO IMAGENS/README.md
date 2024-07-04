# MANIPULANDO IMAGENS
Para manipular imagens em um bot Discord usando Python, você pode usar bibliotecas como `Pillow` (também conhecida como PIL) para realizar tarefas como redimensionamento, corte, adição de texto e muito mais. Abaixo, vou te guiar pelo processo de configurar um bot Discord que manipula imagens e responde com a imagem modificada.

## 1. Configuração Inicial
1. **Instalar as Bibliotecas Necessárias**
   - Primeiro, instale o `discord.py` e o `Pillow`:
     ```bash
     pip install discord.py pillow
     ```

2. **Estrutura do Projeto**
   - Crie um novo projeto e adicione um script Python, por exemplo `bot.py`.

## 2. Implementação do Código
Aqui está um exemplo de como configurar um bot Discord que redimensiona uma imagem enviada pelo usuário:

```python
import discord
from discord.ext import commands
from PIL import Image
import io

# Defina o token do bot
TOKEN = 'YOUR_BOT_TOKEN'

# Defina intents
intents = discord.Intents.default()
intents.message_content = True

# Inicialize o bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento para indicar que o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando para redimensionar uma imagem
@bot.command()
async def resize(ctx, width: int, height: int):
    if not ctx.message.attachments:
        await ctx.send("Por favor, envie uma imagem junto com o comando.")
        return

    # Baixar a imagem
    attachment = ctx.message.attachments[0]
    img_data = await attachment.read()

    # Abrir a imagem
    img = Image.open(io.BytesIO(img_data))

    # Redimensionar a imagem
    img_resized = img.resize((width, height))

    # Salvar a imagem redimensionada em um buffer
    with io.BytesIO() as image_binary:
        img_resized.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='resized_image.png'))

# Iniciar o bot
bot.run(TOKEN)
```

## Explicação do Código
1. **Importações**:
   - `discord`: Para interagir com a API do Discord.
   - `commands`: Para criar comandos que o bot pode responder.
   - `Image` e `io`: Para manipulação de imagens e manipulação de fluxos de dados.

2. **Configuração do Bot**:
   - `TOKEN`: Substitua `'YOUR_BOT_TOKEN'` pelo token do seu bot.
   - `intents`: Definem quais eventos o bot vai ouvir.
   - `bot = commands.Bot(...)`: Inicializa o bot com um prefixo de comando `!`.

3. **Evento `on_ready`**:
   - Imprime uma mensagem no console quando o bot está pronto e conectado.

4. **Comando `resize`**:
   - O comando `!resize` espera dois argumentos: `width` (largura) e `height` (altura).
   - Verifica se há um anexo na mensagem.
   - Baixa a imagem e abre-a usando `Pillow`.
   - Redimensiona a imagem para as dimensões especificadas.
   - Salva a imagem redimensionada em um buffer e envia de volta ao canal.

## Executando o Bot
Salve o script Python e execute-o. No seu servidor Discord, envie uma mensagem com um anexo de imagem e use o comando `!resize <largura> <altura>`, por exemplo:

```
!resize 100 100
```

O bot vai baixar a imagem, redimensioná-la para 100x100 pixels e enviar a imagem redimensionada de volta ao canal.

