from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon import TelegramClient
from telethon import functions
from const import *
from control_center_hendler import *
import time
import os
import tkinter as tk
#from PIL import Image, ImageTk

#api_id = 16321102
#api_hash = 'd94026e2a2f7b4e4be0fde40069782de'
root = tk.Tk()

root.geometry('600x409')
root.resizable(width=0, height=0)

#image1 = Image.open("flag.jpg")
#test = ImageTk.PhotoImage(image1)

#label1 = tk.Label(image=test)
#label1.image = test

#label1.place(x=0, y=0)


#api_id = 16321102
#api_hash = 'd94026e2a2f7b4e4be0fde40069782de'


#Якщо нема config.txt -> Получити данні API і записати в створений config.txt
def redirect():
    os.system("start https://my.telegram.org/%22")

empty_err = tk.Label(root, text = "",)
empty_err.pack()

ver_code_label = tk.Label(root, text = "verification code")
ver_code_tf = tk.Text(height = 1, width=10)

phone_number_label = tk.Label(root, text = "phone nuber")
phone_number_tf = tk.Text(height = 1, width=20)

api_id_Label = tk.Label(root, text = "api id")
api_id_TF = tk.Text(height = 1, width = 15)

api_hash_Label = tk.Label(root, text = "api hash")
api_hash_TF = tk.Text(height = 1, width = 30)


def is_empty(a):
    if not a.split():
        empty_err.config(text = "Заповніть усі поля!")
        return True

    empty_err.config(text="")
    return False


def submit_api_data():
    api_id = api_id_TF.get(1.0, "end-1c")
    if is_empty(api_id):
        return

    api_hash = api_hash_TF.get(1.0, "end-1c")
    if is_empty(api_hash):
        return
    
    config_file = open("config.txt", "w")
    config_file.write("api_id " + str(api_id) + "\napi_hash " + str(api_hash))
    config_file.close()

    api_id_Label.after(1, api_id_Label.destroy)
    api_id_TF.after(1, api_id_TF.destroy)

    api_hash_Label.after(1, api_hash_Label.destroy)
    api_hash_TF.after(1, api_hash_TF.destroy)

    redirect_B.after(1, redirect_B.destroy)
    sumbit_api_B.after(1, sumbit_api_B.destroy)


def enable_ver_code():
    def submit_ver_code():
        ver_code = ver_code_tf.get(1.0, "end-1c")
        if is_empty(ver_code):
            return

        config_file = open("config.txt", "a")
        config_file.write("\nauth_code " + str(ver_code))
        config_file.close()
        
    ver_code_label.pack(pady=5)
    ver_code_tf.pack(pady=5)

    ver_code_button = tk.Button(root, text = "Підтвердити\nверифікаційний код", 
                                fg ="white", bg="#263D42", command=submit_ver_code)
    ver_code_button.pack(pady=5)


def enable_phone():
    def submit_phone():
        phone_number = phone_number_tf.get(1.0, "end-1c")
        if is_empty(phone_number):
            return 
        
        config_file = open("config.txt", "a")
        config_file.write("\nphone_number " + str(phone_number))
        config_file.close()

        phone_number_label.after(1, phone_number_label.destroy)
        phone_number_tf.after(1, phone_number_tf.destroy)
        submit_phone_button.after(1, submit_phone_button.destroy)

    phone_number_label.pack(pady=5)
    phone_number_tf.pack(pady=5)
    
    submit_phone_button = tk.Button(root, text = "Submit", padx = 10, pady = 5, fg ="white", 
                            bg="#263D42", command=submit_phone)
    submit_phone_button.pack()


if not os.path.exists("config.txt"):
    print("fisrst")
    
    api_id_Label.pack(pady=5)
    api_id_TF.pack(pady=5)
    
    api_hash_Label.pack(pady=5)

    api_hash_TF.pack(pady=5)

    button_name = "Зареєструватись на\nhttps://my.telegram.org/%22"
    redirect_B = tk.Button(root, text = button_name, padx = 10, pady = 5, fg ="white", 
                            bg="#263D42", command=redirect)
    redirect_B.pack()
    
    sumbit_api_B = tk.Button(root, text = "Підтвердити api дані", padx = 10, pady = 5, fg ="white", 
                            bg="#263D42", command=submit_api_data)
    sumbit_api_B.pack()

def create_client():
    config = open("config.txt", "r")

    api_id = int(config.readline().split()[1])
    api_hash = config.readline().split()[1]

    config.close()

    client = TelegramClient('anti_putin', api_id, api_hash)

    return client



if not os.path.exists("anti_putin.session"):
    enable_phone()
    root.destroy()
    root.mainloop()

    config = open("config.txt", "r")

    api_id = int(config.readline().split()[1])
    api_hash = config.readline().split()[1]
    phone_number = int(config.readline().split()[1])

    config.close()

    client = TelegramClient('anti_putin', api_id, api_hash)
    client.start(phone=phone_number)
    
    root = tk.Tk()

    root.geometry('600x409')
    root.resizable(width=0, height=0)

    enable_ver_code()

    root.destroy()
    root.mainloop()
else:
    client = create_client()


