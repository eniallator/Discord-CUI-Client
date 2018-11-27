from aiohttp import errors as aio_err
import discord

async def try_login(token):
    client = discord.Client()
    try:
        await client.login(token)
        return client
    except (discord.LoginFailure, discord.HTTPException, TypeError, aio_err.ClientOSError) as err:
        return False

async def login():
    while True:
        token = input('Please enter your discord token: ')
        client = await try_login(token)

        if client:
            print('Successfully logged in')
            return client
        
        print('Error: Invalid token or cannot connect to discord')


async def connect(client):
    try:
        await client.connect()
        print('Successfully connected to discord as ' + client.user.name)
    except (discord.GatewayNotFound, discord.ConnectionClosed):
        print('Error: Could not connect to discord')
