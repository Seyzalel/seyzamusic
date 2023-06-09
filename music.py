import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def _init_(self, seyzalel):
    self.seyzalel = seyzalel
    
  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
      
  @commands.command()
  async def desconectar(self,ctx):
    await ctx.voice_client.disconnect()
  
  @commands.command()
  async def tocar(self,ctx,url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '–reconhece 1 –reconnect_streamed 1 –reconnect_delay_max 5', 'options': '–vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client
    
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpeg0pusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
      
  @commands.command()
  async def pausar(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("Musica foi pausada!")
    
  @commands.command()
  async def resumir(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("Musica voltando!")

def setup(seyzalel):
  seyzalel.add_cog(music(seyzalel))