import json


async def handle(msg, message):
    await message.delete()
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    if msg[1] == name or msg[1] == '*':
        await message.channel.send(f'```[:white_check_mark: ] Node "{name}" gestartet.```')