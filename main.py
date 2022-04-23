import json
import discord
from controllers.matcher import command_matcher

client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(self.user))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))


@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.content.lstrip()[0] == '/':
        await command_matcher(message)  # Match if Command


with open('private.json', 'r') as file:
    data = json.load(file)
client.run(data['token'])
