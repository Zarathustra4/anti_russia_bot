from registration import *

def find_comand(mess,command):
    if mess.find(command) != -1:
        return True
    return False

async def control_center_hendler(chanel_of_control_center):
    messages = client.iter_messages(chanel_of_control_center)

    async for msg in messages:
        if str(type(msg)) == "<class 'telethon.tl.patched.Message'>":
            if find_comand(msg.text, "Comands pannel"):
                if find_comand(msg.text, "❗️start"):
                    return False
                #if find_comand(msg.text, "❗️update config"):
                    #raise Exception("Need to update config file")

    return True

