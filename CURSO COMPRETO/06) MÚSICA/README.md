# MÚSICA
## 1. Importações
```python
import discord
import secreto
```
- **discord**: Importa a biblioteca Discord.py, usada para interagir com a API do Discord.
- **secreto**: Importa um módulo chamado `secreto`, presumivelmente criado para armazenar o token do bot de forma segura.

## 2. Inicialização do Cliente
```python
client = discord.Client()
TOKEN = secreto.seu_token()
```
- **client**: Cria uma instância do cliente Discord. Esta instância é usada para interagir com a API do Discord.
- **TOKEN**: Obtém o token do bot do módulo `secreto`. Este token é usado para autenticar o bot no Discord.

## 3. Evento `on_ready`
```python
@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")
```
- **@client.event**: Um decorador que registra a função como um manipulador de eventos para o cliente Discord.
- **async def on_ready()**: Define uma função assíncrona que é chamada quando o bot está pronto e conectado ao Discord.
- **print(client.user.name)**: Imprime o nome do bot no console.
- **print("Bot online - Olá Mundo!")**: Imprime uma mensagem de confirmação no console indicando que o bot está online.

## 4. Evento `on_message`
```python
@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
      try:
        canal = message.author.voice.voice_channel
        await client.join_voice_channel(canal)
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "Você precisa esta conectado a um canal de voz!")

    if message.content.startswith('!sair'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"O bot não esta conectado em nenhum canal de voz!")
```
- **@client.event**: Um decorador que registra a função como um manipulador de eventos para o cliente Discord.
- **async def on_message(message)**: Define uma função assíncrona que é chamada sempre que uma nova mensagem é recebida.

## Comando `!entrar`
- **if message.content.startswith('!entrar')**: Verifica se o conteúdo da mensagem começa com `!entrar`.
- **canal = message.author.voice.voice_channel**: Obtém o canal de voz em que o autor da mensagem está conectado.
- **await client.join_voice_channel(canal)**: Tenta conectar o bot ao canal de voz.
- **except discord.errors.InvalidArgument**: Captura a exceção se o usuário não estiver conectado a um canal de voz.
- **await client.send_message(message.channel, "Você precisa esta conectado a um canal de voz!")**: Envia uma mensagem de erro ao canal de texto se o usuário não estiver conectado a um canal de voz.

## Comando `!sair`
- **if message.content.startswith('!sair')**: Verifica se o conteúdo da mensagem começa com `!sair`.
- **canaldevoz = client.voice_client_in(message.server)**: Obtém a instância do cliente de voz no servidor.
- **await canaldevoz.disconnect()**: Tenta desconectar o bot do canal de voz.
- **except AttributeError**: Captura a exceção se o bot não estiver conectado a nenhum canal de voz.
- **await client.send_message(message.channel,"O bot não esta conectado em nenhum canal de voz!")**: Envia uma mensagem de erro ao canal de texto se o bot não estiver conectado a um canal de voz.

## 5. Executar o Bot
```python
client.run(TOKEN)
```
- **client.run(TOKEN)**: Inicia o bot usando o token fornecido, permitindo que ele se conecte ao Discord e comece a responder a eventos.

## Observações Importantes
- **Versão da Biblioteca**: O código utiliza métodos e práticas que podem ser de uma versão mais antiga da biblioteca Discord.py. Na versão mais recente (1.5.0+), a maneira de lidar com conexões de voz e enviar mensagens mudou significativamente.
- **Intents**: Com a atualização do Discord.py para a versão 1.5.0+, é necessário habilitar e especificar intents para que o bot possa acessar certas funcionalidades, como ver membros e ler mensagens.

## Versão Atualizada (Se Necessário)
Aqui está uma versão atualizada do código para uma versão mais recente da biblioteca Discord.py:

```python
import discord
import secreto

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True

client = discord.Client(intents=intents)
TOKEN = secreto.seu_token()

@client.event
async def on_ready():
    print(client.user.name)
    print("Bot online - Olá Mundo!")

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
```

Essa versão leva em consideração as mudanças na API do Discord.py e deve funcionar com as versões mais recentes da biblioteca.