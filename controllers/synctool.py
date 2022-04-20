import json
import zlib
from controllers.admintool import is_admin


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    if is_admin(message) is True and (msg[1] == name):
        print('Proceeding...')
        await send_config(msg, message)
    elif is_admin(message) is True and (msg[1] == "push"):
        await load_config(msg, message)


async def send_config(msg, message):
    with open('config.json', 'r') as config:
        config = str(config)
        compressed = zlib.compress(config.encode())
    await message.channel.send('/sync !proceed:->' + str(compressed))


async def load_config(msg, message):
    compressed = bytes(message.split('push !proceed:->', 1))
    config = zlib.decompress(compressed).decode()
    f = open("config.json", "w")
    f.write(config)
    f.close()

# print(zlib.decompress(a).decode())  # outputs original contents of a
