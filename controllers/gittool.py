import json

from controllers.admintool import is_admin


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    if is_admin(message) and msg[1] == name or msg[1] == '*':
        await message.channel.send(f'```\nDer Node {msg[1]} wird gestoppt...\n```')
        exit()
