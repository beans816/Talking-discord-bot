import discord

#import discord token from abcd.py for security
import abcd
from abcd import token

class MyClient(discord.Client):

    async def on_ready(self)

            #replace 'channelID' with the ID of the channel you want the bot to speak in
            channel = client.get_channel(channelID)
            fileObject = open("t.txt", "r")
            #reads everything in file
            data = fileObject.read()
            await channel.send(data)

client = MyClient()
client.run(token)
