import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import Musica
#Se importan las librerias a utilizar en el codigo main

cogs = [Musica]
#Se llama al codigo de los comandos

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())
#Se llaman tanto los comandos como al cliente para que corra

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("OTEwNzIxNzkyOTA4MzQ5NDUw.YZW9ww.jsp6z_BGYWBw8mIrmvjvJoBIVkc")
#Se corre el cliente con el token personal que entrega Discord developer
