import json
from controllers.admintool import is_admin


async def handle(msg, message):
    with open('conf.json', 'r') as f:
        data = json.load(f)
    response = "**-- Help --**\n"
    for item in data['controllers']:
        if data['controllers'][item]['active']:
            if data['controllers'][item]['support'][0] != '*':
                response += '\n**:white_check_mark:  ' + data['controllers'][item]['plugin'].title() + ':**\n' + \
                            data['controllers'][item]['support']
            elif is_admin(message) is True:
                response += '\n**:white_check_mark:  ' + data['controllers'][item]['plugin'].title() + ':**\n' + \
                            data['controllers'][item]['support']
        else:
            response += '\n**:x:  ' + data['controllers'][item]['plugin'].title() + '** -> Zurzeit deaktiviert.\n'
    await message.channel.send(response)
    await message.delete()
