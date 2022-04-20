import json

from controllers.admintool import is_admin


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    if is_admin(message) is True:
        if msg[1] == name:
            await message.channel.send(f'```\nDer Node "{name}" wird aktiviert.\n```')
        else:
            await message.channel.send(f'```\nDer Node {name} wird deaktiviert.\n```')

        with open('conf.json', 'r') as f:
            conf = json.load(f)
        conf['active'] = msg[1]
        with open('conf.json', 'w') as w:
            json.dump(conf, w)

    else:
        await message.channel.send(f'```\nDu hast keine Berrechtigungen für diesen Befehl.\n```')