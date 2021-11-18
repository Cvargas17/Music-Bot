import discord
from discord.ext import commands
import youtube_dl

class musica(commands.Cog):
    def__init__(self, client)
    self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Canal Vacio!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.commmand()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {}
        YDL_OPTIONS = {'format' : "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL-OPTIONS) as ydl:
            info = ydl.extract_info(url, download=false)
            url2 = info['formats'][0]['url']
            source = await discord.FFmegOpusAudio.from_probe(url2,
            **FFMEPG_OPTIONS)
            vc.play(source)


    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Musica Pausada")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Sigue la musica")



def setup(client):
    client.add_cog(musica(client))