from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon import TelegramClient
from telethon import functions
from const import *
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
    os.system("start https://my.telegram.org/%22")


if not os.path.exists("config.txt"):
    redirect()
    api_id = int(input("Print you`r api id: "))
    api_hash = input("Print you`r api hash: ")
    config_file = open("config.txt", "w")
    config_file.write("api_id " + str(api_id) + "\napi_hash " + str(api_hash))
    config_file.close()
    

client = create_client()
