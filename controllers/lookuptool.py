import dns.resolver


async def handle(msg, message):
    results = {}
    modes = ['A', 'AAAA']
    for element in msg:  # Hinzufugen von weiteren Modes mit +MX zB
        if element[0] == "+":
            uelement = element.replace('+', '', 1)
            if not uelement in modes:
                modes.append(uelement)
    for mode in modes:
        try:
            res = dns.resolver.resolve(msg[1], mode)
            results[mode] = res
        except Exception:
            continue
    response = f"```\n[Lookuptool -> {msg[1]}] \n"
    for mode in results:
        response += f"\nRecords ({mode}):\n"
        for result in results[mode]:
            response += "  · "+result.to_text() + ', \n'
    await message.channel.send(response + "```")
