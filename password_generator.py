"""
- Python application to generate password with the
possibility of password recovery.
- Para recuperar uma dada senha, precisa-se digitar
igualmente a mesmas chaves e o mesmo número de
referência.

"""

import tkinter as tk
from tkinter import messagebox
import hashlib
import string
import random

def generate_password():
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    ref = ref_entry.get()
    size = size_var.get()

    if not (key1 and key2 and ref and size):
        messagebox.showinfo("Erro", "Please fill in all fields.")
        return

    hash_object = hashlib.sha256((key1 + key2 + ref).encode())
    password = hash_object.hexdigest()[:size]

    # Add random characters to make the password stronger:
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    while not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(chars) for _ in range(size))

    password_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")  # Sets the size of the application window

key1_label = tk.Label(root, text="Key 1:")
key1_label.pack()
key1_entry = tk.Entry(root)
key1_entry.pack()

key2_label = tk.Label(root, text="Key 2:")
key2_label.pack()
key2_entry = tk.Entry(root)
key2_entry.pack()

ref_label = tk.Label(root, text="Reference:")
ref_label.pack()
ref_entry = tk.Entry(root)
ref_entry.pack()

size_var = tk.IntVar()
size_scale = tk.Scale(root, from_=4, to=12, orient="horizontal", variable=size_var, label="Tamanho da Senha:")
size_scale.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()

