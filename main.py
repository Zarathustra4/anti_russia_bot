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

    chanel_of_chats = await client.get_entity('https://t.me/chat_of_channels')

    victim = await client.get_entity('+380 67 830 53 24')
    #channel = await client.get_entity('https://t.me/pro_pagandaua')
    #await client(JoinChannelRequest(victim))

    i = 2
    while True:
        await client.forward_messages(victim, i, chanel_of_chats)    
        await client.send_message(victim, str(i))
        #time.sleep(0)
        i += 1


    #await client(LeaveChannelRequest(entity))
    
with client:
    client.loop.run_until_complete(main())