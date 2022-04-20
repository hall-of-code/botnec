from icmplib import ping, multiping, traceroute, resolve


async def handle(msg, message):
    print('pingingd')
    await ping_host(msg, message)


async def ping_host(msg, message):
    print('pinging')
    result = ping(msg[1], count=3, interval=0.5, timeout=6)
    response = f"```\n[Pingtool -> {msg[1]}]\n"
    if not result.is_alive:
        failing_point = ping_trace(msg[1], message) or "Error"
        response += "\n" + failing_point + "\n"
    else:
        response += f"\nAVG: {result.avg_rtt} | Maximum: {result.max_rtt} | Minimum: {result.min_rtt} \n"
        if '-t' in msg:
            response += await list_trace(msg, message)
    await message.channel.send(response + "```")


def ping_trace(ip, message):
    results = traceroute(ip, interval=0.06, timeout=2)
    for result in results:
        if not result.is_alive:
            return f"Der {result.distance}te Hop mit der Adresse {result.address} ist nach über 6 Sekunden nicht erreichbar..."


async def list_trace(msg, message):
    results = traceroute(msg[1], interval=0.06, timeout=2)
    response = '\n[Traceroute -> ' + msg[1] + ']\nHop | Adresse                        |  AVG  |  Max  |  Min (ms) \n\n'
    for result in results:
        response += sn('Hop |', result.distance) + '   ' + sn(' Adresse                        |', result.address) + '  ' + sn('  AVG  |', result.avg_rtt) + '  ' + sn('  Max  |', result.max_rtt) + '   ' + sn('  Min (ms) ', result.min_rtt) + '\n'
    return response


def sn(string, fill):
    response = ''
    fill = str(fill)
    string = str(string)
    length = len(string) - 2
    for space in range(length):
        if space <= (len(fill) - 1):
            response += fill[space]
        else:
            response += " "
    return response
