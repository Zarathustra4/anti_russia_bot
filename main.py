from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.errors.common import MultiError
import time
import threading

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'
client = TelegramClient('max', api_id, api_hash)

#Is iptional
#client.flood_sleep_threshold = 0

async def main():
    print("ALL OK")

    me = await client.get_me()
    me = await client.get_entity(me)

    global chanel_of_propaganda
    global chanel_of_chats
    global victim
    global propaganda

    try:
        victim = await client.get_entity('https://t.me/chat_of_channels')
        chanel_of_chats = await client.get_entity('https://t.me/chat_of_channels')
        chanel_of_propaganda = await client.get_entity('https://t.me/pro_pagandaua')
    except FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds+0.5)
    except PeerFloodError:
            print("SPAM ERROR, U get banned, check out @SpamBot for details")
            raise SystemExit
    except MultiError:
            print("MultiError, U get banned, check out @SpamBot for details")
            raise SystemExit

    #await client(JoinChannelRequest(victim))
    
    #trying to cahs everything
    
    users = await client.get_participants(victim)
    propaganda = await client.get_messages(chanel_of_propaganda)
    print(propaganda.total)
    #await client(LeaveChannelRequest(victim))

    """try:
        for user in users:
                if user.id == me.id:
                        continue
                await attack(user)
            # maybe block the user after attack
    except FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds+0.5)
    except PeerFloodError:
            print("SPAM ERROR, U get banned, check out @SpamBot for details")
            raise SystemExit
    except MultiError:
            print("MultiError, U get banned, check out @SpamBot for details")
            raise SystemExit"""


async def attack(user):

        for i in range(2,19):
                await client.forward_messages(user, i, chanel_of_propaganda)
                time.sleep(0.5)
        #except FloodWaitError as e:
            #print('Have to sleep', e.seconds, 'seconds')
            #time.sleep(e.seconds+0.5)
        #except PeerFloodError:
            #print("SPAM ERROR, U get banned, check out @SpamBot for details")
            #raise SystemExit
        #except MultiError:
            #print("MultiError, U get banned, check out @SpamBot for details")
            #raise SystemExit


with client:
    client.loop.run_until_complete(main())
