import json
import importlib
import random
import shlex

from controllers.admintool import is_admin

cache_active = ""
commands = ['/ping', '/lookup', '/help', '/perm', '/track', '/compress', '/git', '/check', '/fallback']
with open('conf.json', 'r') as file:
    cache_data = json.load(file)

cache_active = cache_data['active']
my_name = ""
with open('private.json', 'r') as n:
    d = json.load(n)
    my_name = d['name']


async def command_matcher(message):
    msg = shlex.split(message.content.lstrip())
    if message.guild or is_admin(message) is True:
        if cache_active == my_name:
            for item in commands:
                if msg[0] == item:
                    with open('conf.json', 'r') as f:
                        tools = json.load(f)
                    if tools['controllers'][item] and tools['controllers'][item]['active'] is True:
                        tool = importlib.import_module("controllers." + tools['controllers'][item]['plugin'])
                        await tool.handle(msg, message)
    else:
        await message.channel.send('```\nDie Private Interaktion ist deaktiviert.\n```')
    if msg[0] == "/fallback" or random.randrange(1,7) == 1:
        with open('conf.json', 'r') as f:
            data = json.load(f)
            global cache_active = data['active']

