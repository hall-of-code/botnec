import json
import os
import time

import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        s = message.content.lstrip().split(' ')
        command = s[0] or ''
        value = s[1] or 'none'
        if command == '/git':
            with open('private.json', 'r') as f:
                d = json.load(f)
            if value == d['name'] or value == "*":
                time.sleep(5)
                os.popen('git pull')
                time.sleep(5)
                os.popen('screen -S Botnec python3 main.py')
                await message.channel.send(f'```\nDer Node {value} wird erneut gestartet.\n```')
                time.sleep(2.7)
                await message.channel.send(f'/check {value}')


client = MyClient()

with open('private.json', 'r') as file:
    data = json.load(file)
client.run(data['token'])
