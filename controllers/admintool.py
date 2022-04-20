import json


async def handle(msg, message):
    with open('conf.json', 'r') as f:
        data = json.load(f)
    if str(message.author) in data['roles']['admin']['members']:
        if msg[1] == "add":
            await add_permission(msg, message)
        elif msg[1] == "del":
            await del_permission(msg, message)
        elif msg[1] in ['off', 'false', 'deactivate', 'on', 'true', 'activate']:
            await update_config(msg, message)


async def add_permission(msg, message):
    username = msg[2]
    with open('conf.json', 'r') as f:
        data = json.load(f)
    if username in data['roles']['admin']['members']:
        await message.channel.send(f'` {username} ist berreits Bot-Administrator. `')
    else:
        data['roles']['admin']['members'].append(username)
        updated = data
        print(updated)
        with open('conf.json', 'w') as file:
            json.dump(updated, file)
        await message.channel.send(f'` {username} ist nun Bot-Administrator. `')
    await message.delete()


async def del_permission(msg, message):
    username = msg[2]
    with open('conf.json', 'r') as f:
        data = json.load(f)
    if username not in data['roles']['admin']['members']:
        await message.channel.send(f'` {username} ist berreits entfehrnt. `')
    else:
        data['roles']['admin']['members'].remove(username)
        updated = data
        # print(updated)
        with open('conf.json', 'w') as file:
            json.dump(updated, file)
        await message.channel.send(f'` {username} wurden die Bot-Rechte entzogen. `')
    await message.delete()


async def update_config(msg, message):
    if "perm" not in msg[2]:
        with open('conf.json', 'r') as f:
            data = json.load(f)
        if msg[2][0] != '/':
            msg[2] = '/' + msg[2]
        if msg[1] in ['off', 'false', 'deactivate']:
            print('|| Deactivate', msg[2])
            data['controllers'][msg[2]]['active'] = False
            await message.channel.send(f"` Das {data['controllers'][msg[2]]['plugin'].title()} wurde deaktiviert! `")
        elif msg[1] in ['on', 'true', 'activate']:
            print('|| Activate', msg[2])
            data['controllers'][msg[2]]['active'] = True
            await message.channel.send(f"` Das {data['controllers'][msg[2]]['plugin'].title()} wurde aktiviert. `")
        with open('conf.json', 'w') as file:
            json.dump(data, file)
    await message.delete()


async def is_admin(message):
    with open('conf.json', 'r') as f:
        data = json.load(f)
    if str(message.author) in data['roles']['admin']['members']:
        return True
    return False
