import time
from telethon import TelegramClient
import os

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'

#Якщо нема config.txt -> Получити данні API і записати в створений config.txt
# os.system("start \"\" https://my.telegram.org/")

# ДОПИСАТИ!!!!!
if not os.path.exists("anti_puti.session"):

    #якшо сюда попав, треба залогінити телеграм
    #ше два поля для номера і кода підтвердження
    time.sleep(0)


client = TelegramClient('max', api_id, api_hash)
