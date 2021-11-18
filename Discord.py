import discord
from discord.ext import commands
import music

cogs = [musica]

client = commands.Bot(command_prefix="!", intents = discord.Intents)

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("OTEwNzIxNzkyOTA4MzQ5NDUw.YZW9ww.oO2TBV5VGymevX4E7ECdy54NhzQ")