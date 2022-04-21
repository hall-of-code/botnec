import json
import os
import time

from controllers.admintool import is_admin


async def handle(msg, message):
    with open('private.json', 'r') as file:
        data = json.load(file)
    name = data['name']
    argu = ""
    if len(msg) > 2:
        argu = msg[2]
    if is_admin(message) is True:
        if (msg[1] == name or msg[1] in ["*", '-']) and argu == "-u":
            await message.channel.send(f'```\n[{name}] Der Updater "UP-{name}" wird gestoppt...\n```')
            await update_updater(msg, message, name)
        elif msg[1] == name or msg[1] == '*':
            await message.channel.send(f'```\n[{name}] Der Node "{name}" wird gestoppt...\n```')
            exit()
    else:
        await message.channel.send(f'```\n[{name}] Du hast keine Berrechtigungen für diesen Befehl.\n```')


async def update_updater(msg, message, name):
    try:
        os.popen("screen -X Botnec_Updater quit | grep screen_name | awk '{print $1}' | cut -d. -f1 | xargs kill")
        time.sleep(3)
        # await message.channel.send(f'```\nDer Updater "UP-{name}" wird erneut gestartet...\n```')
        os.popen('screen -S Botnec_Updater -dm python3 updater.py')
    except Exception:
        await message.channel.send(f'```\n[{name}] Es ist ein unerwarteter Fehler aufgetreten.\n```')


