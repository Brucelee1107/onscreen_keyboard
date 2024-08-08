#!/usr/bin/python3

from tkinter import *

root = Tk()
root.geometry('600x200')

cvar = 1
svar = 1

def toggle_var(var):
    var = var + 1
    root.focus_set()
    return var

def toggle_shift(event=None):
    global svar
    svar = toggle_var(svar)

def toggle_caps(event=None):
    global cvar
    cvar = toggle_var(cvar)

def print_char(char):
    def inner(event=None):
        print(char)
        root.focus_set()
    return inner

def print_alternating(chars):
    def inner(event=None):
        print(chars[svar % 2])
        root.focus_set()
    return inner

char_mappings = {
    '~': print_char('~'), '1': print_char('1'), '2': print_char('2'),
    '3': print_char('3'), '4': print_char('4'), '5': print_char('5'),
    '6': print_char('6'), '7': print_char('7'), '8': print_char('8'),
    '9': print_char('9'), '0': print_char('0'), '-': print_alternating(['-', '_']),
    '=': print_alternating(['=', '+']), '{': print_alternating(['[', '{']),
    '}': print_alternating([']', '}']), '\\': print_alternating(['\\', '|']),
    '?': print_alternating(['/', '?']), ':': print_alternating([';', ':']),
    '"': print_alternating(["'", '"']), '<': print_alternating([',', '<']),
    '>': print_alternating(['.', '>']), 'space': print_char(' '),
    'backspace': print_char('\b'), 'tab': print_char('\t'), 'enter': print_char('\n'),
    'caps': toggle_caps, 'shift': toggle_shift
}

letters = 'abcdefghijklmnopqrstuvwxyz'
for letter in letters:
    char_mappings[letter.upper()] = print_alternating([letter, letter.upper()])

frame = Frame(root)
frame.pack(side=TOP)

buttons = [
    ('~', '~'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('0', '0'), ('-', '-'),
    ('+', '='), ('backspace', 'backspace'), ('Tab', 'tab'), ('Q', 'Q'),
    ('W', 'W'), ('E', 'E'), ('R', 'R'), ('T', 'T'), ('Y', 'Y'), ('U', 'U'),
    ('I', 'I'), ('O', 'O'), ('P', 'P'), ('[', '{'), (']', '}'), ('\\', '\\'),
    ('Caps', 'caps'), ('A', 'A'), ('S', 'S'), ('D', 'D'), ('F', 'F'),
    ('G', 'G'), ('H', 'H'), ('J', 'J'), ('K', 'K'), ('L', 'L'), (';', ':'),
    ("'", '"'), ('ENTER', 'enter'), ('Shift', 'shift'), ('Z', 'Z'),
    ('X', 'X'), ('C', 'C'), ('V', 'V'), ('B', 'B'), ('N', 'N'),
    ('M', 'M'), (',', '<'), ('.', '>'), ('/', '?'), ('Shift', 'shift'),
    ('Space', 'space'), ('Exit', 'exit')
]

for text, char in buttons:
    Button(frame, text=text, width='4', bg='black', fg='white', command=char_mappings[char]).pack(side=LEFT)

root.bind('<KeyPress>', lambda event: char_mappings.get(event.keysym.lower(), lambda: None)())
root.mainloop()

