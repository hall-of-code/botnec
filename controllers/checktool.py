import json


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name'] or 'none'
    if msg[1] == name or msg[1] == '*':
        await message.channel.send(f'```Node "{name}" gestartet.```')
        await message.delete()