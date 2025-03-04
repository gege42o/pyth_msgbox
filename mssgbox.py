import tkinter as tk
from tkinter import messagebox
import random

def message2():
    sad = [
        "message here",
    ]
    sad_msg = random.choice(sad)
    message_label.config(text=sad_msg,bg="#ADD8E6")

def message1():
    messages = [
        "message here",
        ]
    random_msg = random.choice(messages)
    message_label.config(text=random_msg,
    bg="#ADD8E6")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("message box")
root.geometry("400x200")
root.configure(bg="#ADD8E6")

message_label = tk.Label(root, text="init text", wraplength=250, font=("Times New Roman", 20))
message_label.pack(pady=20)
message_label.config(bg="#ADD8E6")

button_frame = tk.Frame(root)
button_frame.config(bg="#ADD8E6")
button_frame.pack()

msg1_btn = tk.Button(button_frame, text="message 1", command=message1)
msg1_btn.pack(side=tk.LEFT, fill="x", expand=True, padx=5)
msg1_btn.config(bg="#ADD8E6")

ok_btn = tk.Button(button_frame, text="Ok", command=close_app)
ok_btn.pack(side=tk.RIGHT,fill="x", expand=True, padx=5)
ok_btn.config(bg="#ADD8E6")

msg2_btn = tk.Button(button_frame, text="message 2", command=message2)
msg2_btn.pack(side=tk.BOTTOM,fill="x", expand=True, padx=5)
msg2_btn.config(bg="#ADD8E6")
root.mainloop()