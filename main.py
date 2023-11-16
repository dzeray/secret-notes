import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from cryptography.fernet import *
from tkinter import messagebox, filedialog
import base64
from string import ascii_uppercase
import cryptocode


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 255)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((255 + ord(enc[i]) - ord(key_c)) % 255)
        dec.append(dec_c)
    return "".join(dec)

def encrypted():
    title = title_entry.get()
    secret = secret_text.get(1.0, END)
    key = key_entry.get()
    if len(title) == 0 or len(secret) == 0 or len(key) == 0:
        messagebox.showinfo("Warning!", "Enter your: Title,Secret text, Master key")
    else:
        with open("Secret.txt", "a") as data_file:
            message_encrypted=encode(key, secret)
            data_file.write(f"\n{title}\n{message_encrypted}")
            title_entry.delete(0,END)
            secret_text.delete(1.0,END)
            key_entry.delete(0,END)

def decrypted():
    secret=secret_text.get(1.0,END)
    key = key_entry.get()

    if len(key)== 0 or len(secret)==0:
        messagebox.showinfo(title="Warning!", message="Use the right KEY!!")
    else:
        decrypted_message=decode(key,secret)
        secret_text.delete(1.0,END)
        secret_text.insert(1.0, decrypted_message)

window=tk.Tk()
window.title("Secret Notes")


window.minsize(width=300, height=500)
image=Image.open("topsecret.png")
new_image=image.resize((100,100))
img=ImageTk.PhotoImage(new_image)


top_label=tk.Label(image=img)
top_label.pack()

first_label=tk.Label(text="Enter your title")
first_label.pack(padx=10,pady=10)

title_entry=tk.Entry(width=20)
title_entry.pack()
title_entry.focus()

second_label=tk.Label(text="Enter your secret")
second_label.pack(padx=10,pady=10)

secret_text=tk.Text(width=30, height=10)
secret_text.pack()

key_label=tk.Label(text="Enter master key")
key_label.pack()


key_entry=tk.Entry(width=20, show="*")
key_entry.pack(padx=1, pady=1)
key=str(key_entry.get())


save_button=tk.Button(text="Save & Encrypt", command=encrypted)
save_button.pack(padx=10,pady=10)

if title_entry==0 or secret_text==0 or key_entry==0 :
    messagebox.showwarning("Warning!", "Enter your: Title,Secret text, Master key")

dec_button=tk.Button(text="Decrypt", command=decrypted)
dec_button.pack()



window.mainloop()