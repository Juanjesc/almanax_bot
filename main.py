import requests
import json
import os
from dotenv import load_dotenv

load_dotenv() #This line is used to read the environment variables from the .env file
webhookURL = os.getenv("URL_WEBHOOK")

#Function that obtains the Almanax information of the day.
def obtener_almanax():
    url = "https://alm.dofusdu.de/dofus2/es/almanax?range%5Bsize%5D=1"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        almanax = response.json()
        return almanax
    else:
        return None

#The data is fetched from the api and a message is created.
def generate_data_almanax():
    
    almanax = obtener_almanax()
    print(almanax)
    if almanax is not None:

        tribute = almanax[0]['tribute']
        date = almanax[0]['date']
        item = tribute['item']
        name = item['name']
        quantity = tribute['quantity']
        description = almanax[0]['bonus']['description']
        image_url = item['image_urls']['icon']
        
        #Data structure is created
        data = {
            "username": "Almix_boti",
            "embeds": [
                {
                    "title": f"Fecha: {date}",
                    "description": f":fire: **Bonus:**\n {description}\n\n :gem: **Necesitas:**\n {name} x{quantity}",
                    "thumbnail": {
                        "url": image_url
                    }
                }
            ]
        }
        return data
            
#The event and context parameters are used to trigger the function in AWS Lambda.
def almanax_bot(event, context):
    try:
        headers = {'Content-Type': 'application/json'}
        data = generate_data_almanax()
    except Exception as e:
        print(e)
        data = None

    if data is not None:
        # Sends the POST request with the message
        requests.post(webhookURL, data=json.dumps(data), headers=headers)
    else:
        print("No se ha podido generar el objeto data")
