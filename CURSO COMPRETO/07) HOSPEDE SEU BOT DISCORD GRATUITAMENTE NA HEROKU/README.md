# HOSPEDE SEU BOT DISCORD GRATUITAMENTE NA HEROKU
Hospedar seu bot Discord gratuitamente na Heroku é uma excelente maneira de manter seu bot online 24/7. Aqui estão os passos detalhados para hospedar seu bot no Heroku:

## 1. Preparar o Projeto
1. **Estrutura do Projeto**
   - Crie uma pasta para o seu projeto e adicione seu código do bot nela.
   - Certifique-se de que o código do bot está funcionando localmente antes de continuar.

2. **Criar um `requirements.txt`**
   - Este arquivo lista todas as dependências do projeto. Para Discord.py, adicione a seguinte linha:
     ```
     discord.py
     ```
   - Se você estiver usando outras bibliotecas, adicione-as também.

3. **Criar um `Procfile`**
   - Este arquivo informa ao Heroku como iniciar seu bot. Crie um arquivo chamado `Procfile` (sem extensão) e adicione a seguinte linha:
     ```
     worker: python seu_script.py
     ```
   - Substitua `seu_script.py` pelo nome do arquivo Python que contém seu bot.

4. **Criar um `runtime.txt` (opcional)**
   - Este arquivo define a versão do Python que seu projeto usa. Por exemplo, para usar o Python 3.9, adicione:
     ```
     python-3.9.13
     ```

5. **Adicionar um arquivo `.gitignore`**
   - Para evitar que arquivos desnecessários sejam incluídos no repositório Git, crie um arquivo `.gitignore` com o seguinte conteúdo:
     ```
     __pycache__/
     *.pyc
     .env
     ```

## 2. Configurar o Git
1. **Inicializar o Repositório Git**
   - No terminal, navegue até a pasta do seu projeto e execute:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     ```

## 3. Configurar o Heroku
1. **Criar uma Conta no Heroku**
   - Se você ainda não tem uma conta, registre-se no [Heroku](https://signup.heroku.com/).

2. **Instalar o Heroku CLI**
   - Baixe e instale o Heroku CLI a partir [daqui](https://devcenter.heroku.com/articles/heroku-cli).

3. **Login no Heroku**
   - No terminal, execute:
     ```bash
     heroku login
     ```

4. **Criar um Novo App no Heroku**
   - No terminal, execute:
     ```bash
     heroku create nome-do-seu-app
     ```
   - Substitua `nome-do-seu-app` pelo nome desejado para seu app.

5. **Definir as Configurações do Bot**
   - Defina as variáveis de ambiente, como o token do bot, no Heroku. No terminal, execute:
     ```bash
     heroku config:set DISCORD_TOKEN=seu_token_do_discord
     ```
   - Substitua `seu_token_do_discord` pelo seu token real.

## 4. Desplegar o Bot no Heroku
1. **Adicionar o Remoto Heroku**
   - No terminal, execute:
     ```bash
     git remote add heroku https://git.heroku.com/nome-do-seu-app.git
     ```

2. **Desplegar o Código**
   - No terminal, execute:
     ```bash
     git push heroku master
     ```

3. **Iniciar o Dyno**
   - No terminal, execute:
     ```bash
     heroku ps:scale worker=1
     ```

## Exemplo de Código Completo
Aqui está um exemplo de código para um bot simples que responde a comandos de texto:

```python
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
```

## `requirements.txt`
```
discord.py
```

## `Procfile`
```
worker: python seu_script.py
```

Substitua `seu_script.py` pelo nome do arquivo Python que contém seu bot.

## Considerações Finais
Seguindo esses passos, você poderá hospedar seu bot Discord gratuitamente no Heroku. Certifique-se de verificar os logs do Heroku para depurar qualquer problema que possa surgir:

```bash
heroku logs --tail
```

Assim, seu bot ficará online e funcional 24/7 sem a necessidade de manter um servidor próprio.