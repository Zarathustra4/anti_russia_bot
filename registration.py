from telethon.tl.functions.channels import JoinChannelRequest ,LeaveChannelRequest
from telethon import TelegramClient
from telethon import functions
from registration import *
from const import *
from control_center_hendler import *
import time
import os

api_id = 16321102
api_hash = 'd94026e2a2f7b4e4be0fde40069782de'

client = TelegramClient('anti_putin', api_id, api_hash)
