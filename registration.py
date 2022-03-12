from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon import TelegramClient
from telethon.errors import *
from const import *
import atexit
import time
import os


def create_client():
    config = open("config.txt", "r")

    api_id = int(config.readline().split()[1])
    api_hash = config.readline().split()[1]

    config.close()

    client = TelegramClient('anti_putin', api_id, api_hash)

    return client


#api_id = 16321102
#api_hash = 'd94026e2a2f7b4e4be0fde40069782de'


#Якщо нема config.txt -> Получити данні API і записати в створений config.txt
def redirect():
    print("register you`r own API aplication")
    time.sleep(2)
    print("redirecting...")
    time.sleep(2)
    os.system("start \"\" https://my.telegram.org/")



if not os.path.exists("config.txt"):
    redirect()
    api_id = int(input("Print you`r api id: "))
    api_hash = input("Print you`r api hash: ")
    config_file = open("config.txt", "w")
    config_file.write("api_id " + str(api_id) + "\napi_hash " + str(api_hash) +"\noffline_flag 0")
    config_file.close()
else:
    config = open("config.txt", "r")
    api_id = int(config.readline().split()[1])
    api_hash = config.readline().split()[1]
    config.close()
    def at_exit():
        config = open("config.txt", "r")
        offline_flag = int(config.readlines()[2].split()[1])
        config.close()
        if not offline_flag:
            print("Please, vote Offline in Control Center`s poll")
            time.sleep(5)
            os.system("start \"\" https://t.me/chanel_of_control_center")
            time.sleep(10)
            input("Program ends...")
    # Asks user to vote in poll manualy
    atexit.register(at_exit)

client = create_client()
    