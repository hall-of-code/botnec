import json
import random
import time

from controllers.admintool import is_admin


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    if is_admin(message) is True and (msg[1] == name or msg[1] == '*'):
        time.sleep(random.randrange(1, 3))
        await message.channel.send(f'```[✅] Node "{name}" is running.```')