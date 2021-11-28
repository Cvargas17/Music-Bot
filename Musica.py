import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
#Se importan las librerias a utilizar en el codigo

class musica(commands.Cog):
    def __init__(self, client):
     self.client = client
#Se define la clase musica

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Canal Vacio!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
#Creacion del comando !join
            
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()
#Creacion del comando !disconnect
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format' : "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            ctx.voice_client.play(vc.play(discord.FFmpegPCMAudio(executable = r"C:\Users\Comercia\Desktop\ffmpeg-2021-11-15-git-9e8cdb24cd-full_build\bin\ffmpeg.exe ", source = url2)))


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
   }
           
#Creacion del comando !play
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Musica Pausada")
#Creacion del comando !pause

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Sigue la musica")
#Creacion del comando !resume


def setup(client):
    client.add_cog(musica(client))
#Se define el cliente para poder correr el token de la aplicación
