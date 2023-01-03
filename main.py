import discord
import requests
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Función que obtiene la información del Almanax del día
def obtener_almanax():
    url = "https://alm.dofusdu.de/dofus2/es/almanax?range%5Bsize%5D=1"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        almanax = response.json()
        return almanax
    else:
        return None

@client.event
async def on_message(message):
    if message.channel.name == "dofus-chat":
        if message.content.startswith("!almanax"):
            almanax = obtener_almanax()
            print(almanax)
            if almanax is not None:
                # Envía la información del almanax por Discord
                # Obtiene la información del almanax
                tribute = almanax[0]['tribute']
                date = almanax[0]['date']
                item = tribute['item']
                name = item['name']
                quantity = tribute['quantity']
                description = almanax[0]['bonus']['description']
                image_url = item['image_urls']['icon']
                
                # Construye el mensaje a enviar
                embed = discord.Embed()
                embed.set_thumbnail(url=image_url)
                embed.add_field(name="Fecha: ", value=date, inline=True)
                embed.add_field(name=":fire: Bonus", value=description, inline=False)
                embed.add_field(name=":gem: Necesitas:", value=f"{name} x{quantity}", inline=True)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Ha habido un error al obtener la información del Almanax.")

client.run(TOKEN)