from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import time

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    username = me.username
    print(username)
    print(me.phone)

    entity = await client.get_entity('+380990893264')
    channel = await client.get_entity('https://t.me/pro_pagandaua')
    #await client(JoinChannelRequest(entity))

    for i in range(9, 10):
        await client.forward_messages(entity, i, channel)    
        #time.sleep(0)

    

    #await client(LeaveChannelRequest(entity))
    
with client:
    client.loop.run_until_complete(main())