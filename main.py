import discord
from discord.ext import commands
import music

cogs = [music]

prefixo = ">"
seyzalel = commands.Bot(command_prefix=prefixo, intents=discord.Intents.all())

for i in range (len(cogs)):
  cogs[i].setup(seyzalel)

seyzalel.run("MTA4NjA0NzM4MDc2OTYyNDEyNA.GDjB9F.E7l7aeBiblxhc9GQ8ZAgzHVENgPpp0Zl-LcD5k")