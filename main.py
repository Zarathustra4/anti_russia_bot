from const import *
from registration import *
from control_center_hendler import *
from functions import *

#from telethon.errors.rpcerrorlist import FloodWaitError
#from telethon.errors.rpcerrorlist import PeerFloodError
#from telethon.errors.common import MultiError
#import time


async def main():
    """The main function"""
    
    #Is optional
    client.flood_sleep_threshold = 0

    print("connected to telegram")

    me = await client.get_me()
    me = await client.get_entity(me)

    chanel_of_control_center = await client.get_entity('https://t.me/chanel_of_control_center')

    await client(JoinChannelRequest(chanel_of_control_center))
    print("joined to conrol center")

    while(await control_center_hendler(chanel_of_control_center)):
        time.sleep(delay_btw_cch)

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
    
    links = await create_list_of_links(messages_with_links) #["https://t.me/test_gg_wp"]
    print("created list of links")
    
    # Voting "Online" in poll
    await is_online(chanel_of_control_center)

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
                await attack(user, propaganda)
                time.sleep(delay_btw_attack)
    # Voting "Offline" in poll            
    await is_offline(chanel_of_control_center)
#try:
with client:
    client.loop.run_until_complete(main())
#except Exception:
    #print("Somthing wrong")

