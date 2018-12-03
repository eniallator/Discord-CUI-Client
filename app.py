import asyncio
import discord
from init import login, connect

CLIENT = discord.Client()

STATE = {
    'channel' : None,
    ''
}


@CLIENT.event
async def on_ready():
    print('Bot logged in with name: "' + CLIENT.user.name + '" and id: ' + CLIENT.user.id)


@CLIENT.event
async def on_message(message):
    print('[' + str(message.author) + ']: ' + message.content)


if __name__ == '__main__':
    try:
        LOOP = asyncio.get_event_loop()
        LOOP.run_until_complete(login(CLIENT))
        LOOP.run_until_complete(connect(CLIENT))
        LOOP.close()
    except KeyboardInterrupt as err:
        print('\r\n\r\nExiting discord CUI client.')
