import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#initialize discord client
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

#message handler
async def SendMessage(message: Message, UserMessage: str):
    if not UserMessage:
        return
    
    try:
        reponse = get_response(UserMessage, message.author)
        await message.channel.send(reponse)
    except Exception:
        return

#event handlers
@client.event
async def on_ready():
    print(f"{client.user} has gone online!")

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    await SendMessage(message, message.content)

#main function
def main():
    client.run(TOKEN)
    

if __name__ == "__main__":
    main()