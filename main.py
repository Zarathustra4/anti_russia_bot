from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError, PeerFloodError
from telethon.errors.common import MultiError
import time
import threading

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'
client = TelegramClient('anti_putin', api_id, api_hash)

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
    
    users = client.iter_participants(victim, aggressive = True)
    propaganda = client.iter_messages(chanel_of_propaganda)

    #await client(LeaveChannelRequest(victim))

    try:
        async for user in users:
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
            raise SystemExit
    
    


async def attack(user):

    async for message in propaganda:
        try:
            await client.forward_messages(user, message)    
            time.sleep(0.1)
        except FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds+0.5)
        except PeerFloodError:
            print("SPAM ERROR, U get banned, check out @SpamBot for details")
            raise SystemExit
        except MultiError:
            print("MultiError, U get banned, check out @SpamBot for details")
            raise SystemExit


with client:
    client.loop.run_until_complete(main())