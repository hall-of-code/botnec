import json
import os
import random
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
        msg2 = ''
        if len(s) > 2:
            msg2 = s[2]
        with open('conf.json', 'r') as conf:
            config = json.load(conf)
        if command == '/git' and str(message.author) in config['roles']['admin']['members']:
            with open('private.json', 'r') as f:
                d = json.load(f)
            if (value == d['name'] or value in ['*', '-']) and msg2 == '-u':
                time.sleep(1)
                os.popen('git stash')
                time.sleep(2)
                os.popen('git pull')
                time.sleep(2)
                await message.channel.send(f'```\nDer Updater "UP-{d["name"]}" wird erneut gestartet.\n```')
                exit()
            elif value == d['name'] or value == "*":
                time.sleep(1)
                os.popen('git stash')
                time.sleep(4)
                os.popen('git pull')
                time.sleep(5)
                os.popen('screen -S Botnec -dm python3 main.py')
                await message.channel.send(f'```\nDer Node "{d["name"]}" wird erneut gestartet.\n```')
                time.sleep(random.randrange(4, 13))
                await message.channel.send(f'/check {d["name"]}')


client = MyClient()

with open('private.json', 'r') as file:
    data = json.load(file)
client.run(data['token'])
