# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 16:30:23 2025

@author: HP V15 (493178410)
"""

from tkinter import *

root = Tk()
root.title("Calculator<3")
root.geometry("320x400")
root.configure(bg="#FFC0CB")  

entry = Entry(root, font=("Arial", 20), borderwidth=5, relief=RIDGE, justify=RIGHT)
entry.pack(fill=BOTH, ipadx=8, ipady=10, padx=10, pady=20)

def button_click(symbol):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + symbol)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_clear():
    entry.delete(0, END)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = Frame(root, bg="#FFC0CB")
    frame.pack(expand=True, fill=BOTH)
    for btn_text in row:
        if btn_text == 'C':
            btn = Button(frame, text=btn_text, font=("Arial", 18), bg="white", fg="black",
                         command=button_clear)
        elif btn_text == '=':
            btn = Button(frame, text=btn_text, font=("Arial", 18), bg="white", fg="black",
                         command=button_equal)
        else:
            btn = Button(frame, text=btn_text, font=("Arial", 18), bg="white", fg="black",
                         command=lambda x=btn_text: button_click(x))
        btn.pack(side=LEFT, expand=True, fill=BOTH, padx=2, pady=2)

root.mainloop()


