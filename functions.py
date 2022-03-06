from registration import *

async def attack(user, propaganda):
    """The functions of attack"""
    
    #attack part
    msg_c = 0
    print("attack user: " + str(user.username))
    async for msg in propaganda:
        if str(type(msg)) == "<class 'telethon.tl.patched.Message'>":
                await client.forward_messages(user, msg)
                print("message sent")
                time.sleep(delay_btw_msg)
                msg_c+=1
                if msg_c == msg_per_buffer:
                    print("delay...")
                    time.sleep(delay_btw_buffers)
                    msg_c = 0
    
    #archive part
    dialogs = client.iter_dialogs()
    async for dialog in dialogs:
            if user.id == dialog.entity.id:
                await client.edit_folder(dialog, 1)
                await client(functions.contacts.BlockRequest(id=user.username))
                print("chat with user: "+ str(user.username) + " deleted")
                break


async def create_list_of_links(messages_with_links):
    """The functions create_list_of_links"""
    list_of_links = []

    async for message in messages_with_links:
            if str(type(message)) == "<class 'telethon.tl.patched.Message'>":
                link = find_links(message.text)
                if type(link) == type(""):
                        list_of_links.append(link)

    return list_of_links


def find_links(text):
    """The functions find links from string text"""

    prefix = ['t.me', '@']
    
    links = []
    text = text.split()

    for i in range(len(text)):
        if text[i].find(prefix[0]) != -1:
            links.append(text[i])
        

    if links != []:
        return str(links[0])


async def is_online(chanel_of_control_center):
    msg = client.iter_messages(chanel_of_control_center)
    async for poll in msg:
        await poll.click(text = "🟢Online🟢")
    print("🟢Online🟢")


async def is_offline(chanel_of_control_center):
    msg = client.iter_messages(chanel_of_control_center)
    async for poll in msg:
        await poll.click(text = "🔴Offline🔴")
    print("🔴Offline🔴")
    
