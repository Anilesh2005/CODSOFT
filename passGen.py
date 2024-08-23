
from tkinter import *
root=Tk()
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

root.title("Password Generator")

length_label = Label(root, text="Enter password length:")
length_label.pack()

length_entry = Entry(root)
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=lambda: password_entry.insert(0, generate_password(int(length_entry.get()))))
generate_button.pack()

password_entry = Entry(root, width=40)
password_entry.pack()

copy_button = Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack()

root.mainloop()