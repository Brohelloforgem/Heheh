import os
import time
from keep_alive import keep_alive
try:
    import discord
except:
    from setup import install
    install()
    import discord

print("""\
██╗░░░██╗░█████╗░██╗░█████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░
██║░░░██║██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║
░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║
░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
**Version: 1.0.0**""")
time.sleep(0.5)
client = discord.Client(intents=discord.Intents.default())
Token = os.getenv("TOKEN")
Id = 1256896417822281790


@client.event
async def on_ready():
    voice_channel = client.get_channel(Id) 
    await client.change_presence(activity = discord.Streaming(name = "Gem on Top", url = "https://twitch.tv/gemop"))
    await voice_channel.connect()
  
    print('Logged in as {0.user}'.format(client))
    print('Connected to voice channel: {}'.format(voice_channel))
    
keep_alive()
client.run(Token, bot = False)

