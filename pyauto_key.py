#!/usr/bin/python3

import tkinter as tk
import pyautogui

is_caps = False

def create_keyboard(root):
    keys = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Delete'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Caps'],
        ['                    ','Special']
    ]

    for row in keys:
        key_row = tk.Frame(root)
        key_row.pack(side='top', expand='yes', fill='both')
        for key in row:
            button = tk.Button(key_row, text=key, command=lambda k=key: key_press(k))
            button.pack(side='left', expand='yes', fill='both')

def key_press(key):
    global is_caps, is_shift

    if key == "                    ":
        pyautogui.press('space')
    elif key == "Delete":
        pyautogui.press('backspace')
    elif key == "Caps":
        is_caps = not is_caps
    elif key == "Special":
        switch_to_special_characters()
    else:
        if is_caps:
            pyautogui.press(key.upper())
        else:
            pyautogui.press(key.lower())

def switch_to_special_characters():
    special_keys = [
        ['~','!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '='],
        ['`','[', ']', '{', '}', '|', '\\', ':', ';', '\'', '\"'],
        ['+', '-', '/', '*','<', '>', ',', '.', '/', '?'],
        ['                    ', 'ABC']
    ]
    
    # Clear existing keyboard
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create special character keyboard
    for row in special_keys:
        key_row = tk.Frame(root)
        key_row.pack(side='top', expand='yes', fill='both')
        for key in row:
            button = tk.Button(key_row, text=key, command=lambda k=key: key_press_special(k))
            button.pack(side='left', expand='yes', fill='both')

def key_press_special(key):
    global is_caps
    
    if key == "Space":
        pyautogui.press('space')
    elif key == "Delete":
        pyautogui.press('backspace')
    elif key == "Caps":
        is_caps = not is_caps
    elif key == "ABC":
        switch_to_alphabet_characters()
    else:
        pyautogui.press(key)

def switch_to_alphabet_characters():
    # Clear existing keyboard
    for widget in root.winfo_children():
        widget.destroy()
    
    # Create alphabet keyboard
    create_keyboard(root)

root = tk.Tk()
root.title("Virtual Keyboard")
create_keyboard(root)
root.mainloop()

