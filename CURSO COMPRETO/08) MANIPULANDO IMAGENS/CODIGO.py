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
