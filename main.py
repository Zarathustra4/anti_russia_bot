from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from registration import *
from functions import *
from const import *
#from telethon.errors.rpcerrorlist import FloodWaitError
#from telethon.errors.rpcerrorlist import PeerFloodError
#from telethon.errors.common import MultiError
#import time

#Is optional
client.flood_sleep_threshold = 0

async def main():
    """The main function"""
    print("connected to telegram")

    me = await client.get_me()
    me = await client.get_entity(me)

    chanel_of_chats = await client.get_entity('https://t.me/chat_of_channels')
    chanel_of_propaganda = await client.get_entity('https://t.me/pro_pagandaua')

    await client(JoinChannelRequest(chanel_of_chats))
    print("joined chat of links")

    await client(JoinChannelRequest(chanel_of_propaganda))
    print("joined chat of propaganda")

    propaganda = client.iter_messages(chanel_of_propaganda)
    print("copied propaganda messages")

    messages_with_links = client.iter_messages(chanel_of_chats)
    print("copied link messages")
    
    links = await create_list_of_links(messages_with_links)
    print("created list of links")
    
    for link in links:
        victim = await client.get_entity(link)

        await client(JoinChannelRequest(victim))
        print("joined chat")

        #trying to cahs everything
    
        users = client.iter_participants(victim, aggressive = True)
        print("copied user info")
        

        await client(LeaveChannelRequest(victim))
        print("leaved chat")

        async for user in users:
                if user.id == me.id:
                        continue
                #await attack(user, propaganda)
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    if user.id == dialog.entity.id:
                        await dialog.archive()
                        #print("chat with user: "+ str(user.username) + " deleted")
                        #print(dialog.entity)
                        break


with client:
    client.loop.run_until_complete(main())

