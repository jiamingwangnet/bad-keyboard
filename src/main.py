from tkinter import *
from tkinter import ttk, Text
from pyperclip import copy as cpy

root = Tk()
root.title("Bad keyboard")
root.geometry("310x400")
root.resizable(False, False)

main = ttk.Frame(root, padding=5, width=350, height=250)
main.grid(column=0, row=1)

ctrl = ttk.Frame(main, padding=20, relief="solid", width=250, height=50)
ctrl.place(relx=0.5, rely=0.36, anchor="center")
ctrl.grid(column=0, row=1)

dis = ttk.Frame(root, padding=0)
dis.grid(column=0, row=0)

out = ttk.Frame(root, padding=10, relief="solid", width=250, height=50)
out.grid(column=0, row=2)

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
    global textarea
    textarea.delete(END, END)

def copy_all():
    global textarea
    cpy(textarea.get(0.0, END))

def write():
    global textarea
    textarea.insert(INSERT, chr(output))

def copy():
    cpy(chr(output))

def clear_all():
    global textarea
    textarea.delete(0.0, END)

ttk.Button(ctrl, text="+", command=increase).grid(column=2, row=3, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Copy Char", command=copy).grid(column=1, row=3, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="-", command=decrease).grid(column=0, row=3, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="<<", command=shift_left).grid(column=0, row=4, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Write", command=write).grid(column=1, row=4, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text=">>", command=shift_right).grid(column=2, row=4, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="Latin Lower", command=lat_down).grid(column=0, row=5, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Latin Upper", command=lat_up).grid(column=1, row=5, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Numbers", command=num_pad).grid(column=2, row=5, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="Backspace", command=bkspace).grid(column=0, row=6, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Copy All", command=copy_all).grid(column=1, row=6, padx=(5, 5), pady=(5, 5))
ttk.Button(ctrl, text="Set to 0x00", command=clear).grid(column=2, row=6, padx=(5, 5), pady=(5, 5))

ttk.Button(ctrl, text="Clear", command=clear_all).grid(column=1, row=7, padx=(5, 5), pady=(5, 5))

textarea = Text(out, width=30, height=5)
textarea.grid(column=0, row=7, padx=(5, 5), pady=(5, 5))

root.mainloop()