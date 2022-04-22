from tkinter import *
from tkinter import ttk
from pyautogui import press, typewrite
from pyperclip import copy as cpy

root = Tk()
root.title("Bad keyboard")
root.geometry("350x250")
root.resizable(False, False)

main = ttk.Frame(root, padding=5, width=350, height=250)
main.grid(column=0, row=1)

ctrl = ttk.Frame(main, padding=20, relief="solid", width=250, height=50)
ctrl.place(relx=0.5, rely=0.36, anchor="center")

dis = ttk.Frame(root, padding=0)
dis.grid(column=0, row=0)

output = 0x0000

hex_dis = ttk.Label(dis, text=hex(output), font="Arial 15")
hex_dis.grid(column=0, row=0)

char_dis = ttk.Label(dis, text=chr(output), font="Arial 15")
char_dis.grid(column=0, row=1)

def update():
    global hex_dis, char_dis
    hex_dis.config(text=hex(output))
    char_dis.config(text=chr(output))

def increase():
    global output
    output += 0x1
    update()

def decrease():
    global output
    output -= 0x1
    update()

def shift_left():
    global output
    output *= 0x10
    update()

def shift_right():
    global output
    output //= 0x10
    update()

def clear():
    global output
    output = 0x0000
    update()

def lat_up():
    global output
    output = 0x41
    update()

def lat_down():
    global output
    output = 0x61
    update()

def num_pad():
    global output
    output = 0x30
    update()

def bkspace():
    press("backspace")

def enter():
    press("enter")

def write():
    typewrite(chr(output))

def copy():
    cpy(chr(output))

ttk.Button(ctrl, text="Increase", command=increase).grid(column=0, row=3, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Copy", command=copy).grid(column=1, row=3, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Decrease", command=decrease).grid(column=2, row=3, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="<<", command=shift_left).grid(column=0, row=4, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Write", command=write).grid(column=1, row=4, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text=">>", command=shift_right).grid(column=2, row=4, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="Latin Lower", command=lat_down).grid(column=0, row=5, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Latin Upper", command=lat_up).grid(column=1, row=5, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Number Pad", command=num_pad).grid(column=2, row=5, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="Backspace", command=bkspace).grid(column=0, row=6, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Enter", command=enter).grid(column=1, row=6, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Clear", command=clear).grid(column=2, row=6, padx=(5, 5), pady=(5, 5))

root.mainloop()