from registration import *

async def control_center_hendler(chanel_of_control_center):
    messages = client.iter_messages(chanel_of_control_center)

    async for msg in messages:
        if str(type(msg)) == "<class 'telethon.tl.patched.Message'>":
            print(msg.text)

    return True

