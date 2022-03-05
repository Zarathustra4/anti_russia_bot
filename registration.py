import time
from telethon import TelegramClient
import os

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'

# ДОПИСАТИ!!!!!
if not os.path.exists("anti_putin.session"):

    print("U need to register Telegram api app")
    print("Redirrecting...")

    os.system("start \"\" https://my.telegram.org/")

    #api_id = int(input())
    #api_hash = input()
print("U alredy have an session")

client = TelegramClient('max', api_id, api_hash)


