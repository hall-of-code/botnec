import json
import importlib
import random
import shlex

from controllers.admintool import is_admin

commands = ['/ping', '/lookup', '/help', '/perm', '/track', '/compress', '/git', '/check', '/fallback']

my_name = ""
with open('private.json', 'r') as n:
    d = json.load(n)
my_name = d['name']


async def command_matcher(message):
    msg = shlex.split(message.content.lstrip())
    if message.guild or is_admin(message) is True:
        with open('conf.json', 'r') as c:
            dt = json.load(c)
        cache_active = dt['active']
        if (cache_active == my_name) or msg[0] == '/fallback':
            for item in commands:
                if msg[0] == item:
                    with open('conf.json', 'r') as f:
                        tools = json.load(f)
                    if tools['controllers'][item] and tools['controllers'][item]['active'] is True:
                        tool = importlib.import_module("controllers." + tools['controllers'][item]['plugin'])
                        await tool.handle(msg, message)
    else:
        await message.channel.send('```\nDie Private Interaktion ist deaktiviert.\n```')

