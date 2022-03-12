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
    try:
        me = await client.get_me()
        me = await client.get_entity(me)

        chanel_of_control_center = await client.get_entity('https://t.me/chanel_of_control_center')

        await client(JoinChannelRequest(chanel_of_control_center))
        print("joined to conrol center")

        while(await control_center_hendler(chanel_of_control_center)):
            time.sleep(delay_btw_cch)

        chanel_of_chats = await client.get_entity('https://t.me/chat_of_channels')

        await client(JoinChannelRequest(chanel_of_chats))
        print("joined chat of links")

        messages_with_links = client.iter_messages(chanel_of_chats)
        print("copied link messages")
    
        links = await create_list_of_links(messages_with_links) #["https://t.me/test_gg_wp"]
        print("created list of links")
    except FloodWaitError as e:
            print('Flood wait for ', e.seconds)
            print("You need to wait " + str(e.seconds) + " seconds before start again")
            raise SystemExit
            
    # Voting "Online" in poll
    await is_online(chanel_of_control_center)

    for link in links:
        try:
         
            victim = await client.get_entity(link)

            print("reporting " + victim.title)

            await client(JoinChannelRequest(victim))
            print("joined chat")

            time.sleep(delay_btw_buffers)

            await attack(victim)
            print("report sended")

            time.sleep(delay_btw_buffers)
        
            await client(LeaveChannelRequest(victim))
            print("leaved chat")
   
            time.sleep(delay_btw_attack)
        except FloodWaitError as e:
            print('Flood wait for ', e.seconds)
            print("You need to wait " + str(e.seconds) + " seconds before start again")
            print("Strongly recomend to NOT start program again, before interaption for " + str(e.seconds) + " seconds")
            time.sleep(10)
            raise SystemExit
        except ChannelPrivateError:
            pass
    # Voting "Offline" in poll            
    await is_offline(chanel_of_control_center)

with client:
    client.loop.run_until_complete(main())


