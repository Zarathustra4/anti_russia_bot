from registration import *


async def attack(user):
        await client(functions.account.ReportPeerRequest(
            peer = user,
            reason = types.InputReportReasonFake(), 
            message = "Fake info about war in Ukraine"
        ))
        


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
    a_file = open("config.txt", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = "offline_flag 0"

    a_file = open("config.txt", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    print("Online")


async def is_offline(chanel_of_control_center):
    msg = client.iter_messages(chanel_of_control_center)
    async for poll in msg:
        await poll.click(text = "🔴Offline🔴")
    a_file = open("config.txt", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = "offline_flag 1"

    a_file = open("config.txt", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    print("Offline")
    input("Program ends...")
    
