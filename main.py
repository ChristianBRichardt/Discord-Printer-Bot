import discord
import subprocess
import os

generel_id = 1407704842004070443
image_types = {"png", "jpeg", "jpg", "pdf"}

class Client(discord.Client):
    
    async def on_ready(self):
        os.system("echo Penis")
        print(f'{self} online!')
        channel = Client.get_channel(self, generel_id)
        await channel.send('Online!')
    
    async def on_message(self, message):
        if message.content.lower().startswith("ci"): # CI (check ink)
            command = "ink -p usb"
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip()

            channel = Client.get_channel(self, generel_id)
            await channel.send(output)
        
        if message.content.lower().startswith("cf"): # CF (check files)
            command = "ls"
            wd = os.getcwd()
            os.chdir("attachments")
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip()
            os.chdir(wd)

            channel = Client.get_channel(self, generel_id)
            await channel.send(output)
        
        if message.content.lower().startswith("rf"):
            command = "ls"
            wd = os.getcwd()
            os.chdir("attachments")
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip()            
            files = output.splitlines()
            for file in files:
                os.remove(file)
            os.chdir(wd)

            channel = Client.get_channel(self, generel_id)
            await channel.send('All files have been removed!')

        for attachment in message.attachments: # Downloads and prints files
            if any(attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save(f'attachments/{attachment.filename}')
                os.system(f'lp {attachment.filename}')

                channel = Client.get_channel(self, generel_id)
                await channel.send('Starting to print!')
        

                

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('TOKEN_HERE')