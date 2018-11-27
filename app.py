import asyncio
from init import login

async def main():
    try:
        client = await login()
    except KeyboardInterrupt as err:
        print('\r\n\r\nExiting discord CUI client.')


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
    except (RuntimeError, OSError) as err:
        print('')
