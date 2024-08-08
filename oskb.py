#!/usr/bin/python3

import tkinter as tk
import pyautogui

caps_lock = False
shift = False

def on_key_press(key):
    global caps_lock, shift
    if key == '⌫':  # Backspace symbol
        pyautogui.press('backspace')
    elif key == '⇪':  # Caps Lock symbol
        caps_lock = not caps_lock
        update_keys()
    elif key == '␣':  # Space symbol
        pyautogui.press('space')
    elif key == '⏎':  # Enter symbol
        pyautogui.press('enter')
    elif key == "?123" or key == "Abc":
        shift = not shift
        create_keyboard(root)  # Update the entire keyboard layout when shift is toggled
    else:
        if shift and key.isalpha():
            key = key.upper()
            shift = False  # Reset shift after a single use
        elif caps_lock and key.isalpha():
            key = key.upper()
        pyautogui.typewrite(key)
        update_keys()

def update_keys():
    for button, key in zip(key_buttons, [key for row in (shift_keys if shift else alpha_keys) for key in row]):
        if key == '⇪':  # Caps Lock symbol
            button.config(bg='yellow' if caps_lock else 'grey')
        elif key == "?123" or key == "Abc":
            button.config(bg='yellow' if shift else 'grey')
        else:
            button.config(text=key.upper() if (caps_lock or shift) and key.isalpha() else key)

def create_keyboard(root):
    global key_buttons
    key_buttons = []

    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

    for row in (shift_keys if shift else alpha_keys):
        key_row = tk.Frame(root)
        key_row.pack(expand=True, fill='both')

        for key in row:
            button = tk.Button(key_row, text=key, command=lambda k=key: on_key_press(k))
            button.pack(side='left', expand=True, fill='both')
            key_buttons.append(button)

    update_keys()

alpha_keys = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '⌫'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['⇪', 'z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ["?123", '.', ',', '?', '!', '@', '#', '$', '%', '&'],
    ['␣', '⏎']
]

shift_keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '⌫'],
    ['-', '/', ':', ';', '(', ')', '$', '&', '@', '"'],
    ['⇪', '+', '=', '*', '_', '\\', '|', '~', "'"],
    ['Abc', '[', ']', '{', '}', '<', '>', '^', '!', '?'],
    ['␣', '⏎']
]

geometry = '400x200'
root = tk.Tk()
root.title("Virtual Keyboard")
root.geometry(geometry)
create_keyboard(root)
update_keys()

root.mainloop()
