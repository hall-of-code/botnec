import json

import discord
from controllers.matcher import command_matcher


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.lstrip()[0] == '/':
            await command_matcher(message)  # Match if Command

    async def on_raw_reaction_add(self, reaction):
        if reaction.emoji.name == '❌':
            guild = await self.fetch_guild(reaction.guild_id)
            channel = guild
            # message = await channel.fetch_message(reaction.message_id)
            print(channel)


client = MyClient()

with open('conf.json', 'r') as file:
    data = json.load(file)
client.run(data['token'])
