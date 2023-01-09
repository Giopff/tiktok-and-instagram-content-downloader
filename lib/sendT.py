from telethon import TelegramClient
import asyncio
import os
def op():
    with open("../data/auth.txt") as f:
        api_id = f.readline().strip()
        api_hash = f.readline().strip()
    return api_id, api_hash

async def sendTel():
    api_id, api_hash = op()
    async with TelegramClient('', api_id, api_hash) as client:
        await client.connect()
        channel = await client.get_entity('telegram channel link')
        for video in os.listdir('./vids'):
            await client.send_file(channel, './vids/'+video)


def sendTelmain():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(sendTel())
        loop.close()
    except Exception as err:
        print(err)
        exit(1)

if __name__ == '__main__':
    print(op())
