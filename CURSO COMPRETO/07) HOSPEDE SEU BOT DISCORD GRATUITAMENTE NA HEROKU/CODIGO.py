import discord
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True

client = discord.Client(intents=intents)
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
        try:
            canal = message.author.voice.channel
            if canal:
                await canal.connect()
            else:
                await message.channel.send("Você precisa estar conectado a um canal de voz!")
        except discord.errors.ClientException:
            await message.channel.send("O bot já está conectado a um canal de voz!")
        except AttributeError:
            await message.channel.send("Você precisa estar conectado a um canal de voz!")

    if message.content.startswith('!sair'):
        try:
            canaldevoz = message.guild.voice_client
            if canaldevoz:
                await canaldevoz.disconnect()
            else:
                await message.channel.send("O bot não está conectado em nenhum canal de voz!")
        except AttributeError:
            await message.channel.send("O bot não está conectado em nenhum canal de voz!")

client.run(TOKEN)
