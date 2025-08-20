import discord
import os

generel_id = 1407704842004070443
image_types = {"png", "jpeg", "jpg", "pdf"}

class Client(discord.Client):
    
    async def on_ready(self):
        os.system("echo Penis")
        print(f'{self} online!')
        # channel = Client.get_channel(self, generel_id)
        # await channel.send('Online!')
    
    async def on_message(self, message):
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save(f'attachments/{attachment.filename}')
                os.system(f'lp {attachment.filename}')
                channel = Client.get_channel(self, generel_id)
                await channel.send('Starting to print!')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('BOT_TOKEN_HERE')