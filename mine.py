#!/usr/bin/python3

from tkinter import *
import subprocess

def send_keystroke(key):
    # Send the keystroke to the active window
    subprocess.call(['xdotool', 'type', key])

def send_key_command(command):
    # Send a specific key command to the active window (like Enter, Backspace)
    subprocess.call(['xdotool', 'key', command])

def shift_toggle():
    global shift_pressed
    shift_pressed = not shift_pressed

def caps_toggle():
    global caps_locked
    caps_locked = not caps_locked

def char_switcher(char1, char2):
    return char1 if shift_pressed else char2

def type_char(char1, char2=None):
    if char2:
        char = char_switcher(char1, char2)
    else:
        char = char1.upper() if caps_locked else char1.lower()
    send_keystroke(char)

def type_digit(digit):
    send_keystroke(str(digit))

root = Tk()

shift_pressed = False
caps_locked = False

# Simplify button creation with loops
def create_button(frame, text, command, width=None):
    Button(frame, text=text, bg="black", fg="white", command=command, width=width).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=TOP)

special_chars = ["~", "-", "=", "{", "}", "\\", "/", ":", "'", ",", ".", "?"]
special_funcs = [lambda: type_char('~'), lambda: type_char('_', '-'), lambda: type_char('+', '='),
                 lambda: type_char('{', '['), lambda: type_char('}', ']'), lambda: type_char('|', '\\'),
                 lambda: type_char('?', '/'), lambda: type_char(':', ';'), lambda: type_char('"', "'"),
                 lambda: type_char('<', ','), lambda: type_char('>', '.'), lambda: type_char('?', '/')]

for char, func in zip(special_chars, special_funcs):
    create_button(frame, char, func)

digits = range(10)
for digit in digits:
    create_button(frame, str(digit), lambda d=digit: type_digit(d))

create_button(frame, "Backspace", lambda: send_key_command('BackSpace'))

frame1 = Frame(root)
frame1.pack()

create_button(frame1, "Tab", lambda: send_key_command('Tab'))

letters = "QWERTYUIOP"
for letter in letters:
    create_button(frame1, letter, lambda l=letter: type_char(l))

frame2 = Frame(root)
frame2.pack()

create_button(frame2, "CapsLK", caps_toggle)

letters = "ASDFGHJKL"
for letter in letters:
    create_button(frame2, letter, lambda l=letter: type_char(l))

create_button(frame2, ";", lambda: type_char(';', ':'))
create_button(frame2, "'", lambda: type_char("'", '"'))
create_button(frame2, "Enter", lambda: send_key_command('Return'))

frame3 = Frame(root)
frame3.pack()

create_button(frame3, "Shift", shift_toggle)

letters = "ZXCVBNM"
for letter in letters:
    create_button(frame3, letter, lambda l=letter: type_char(l))

create_button(frame3, ",", lambda: type_char(',', '<'))
create_button(frame3, ".", lambda: type_char('.', '>'))
create_button(frame3, "/", lambda: type_char('/', '?'))
create_button(frame3, "Shift", shift_toggle)

frame4 = Frame(root)
frame4.pack()

create_button(frame4, "Exit", root.quit)
create_button(frame4, "Space", lambda: send_keystroke(' '), width=15)

root.mainloop()

