import json
import importlib
import shlex

from controllers.admintool import is_admin

commands = ['/ping', '/lookup', '/help', '/perm', '/track', '/compress', '/git', '/check', '/sync']


async def command_matcher(message):
    msg = shlex.split(message.content.lstrip())
    if message.guild or is_admin(message) is True:
        for item in commands:
            if msg[0] == item:
                with open('conf.json', 'r') as f:
                    tools = json.load(f)
                if tools['controllers'][item] and tools['controllers'][item]['active'] is True:
                    tool = importlib.import_module("controllers." + tools['controllers'][item]['plugin'])
                    await tool.handle(msg, message)
    else:
        await message.channel.send('```\nDie Private Interaktion ist deaktiviert.\n```')
