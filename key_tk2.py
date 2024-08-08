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
        elif caps_lock and key.isalpha():
            key = key.upper()
        pyautogui.typewrite(key)

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
            button = tk.Button(key_row, text=key, width=4, height=3, command=lambda k=key: on_key_press(k))
            button.pack(side='left', expand=True, fill='both')
            button.bind('<ButtonRelease-1>', lambda e, k=key: on_key_release(k))
            key_buttons.append(button)

    update_keys()

def on_key_release(key):
    pass  # Handle key release events if necessary

# def focus_in(event):
#     pass  # No need to open onboard

# def focus_out(event):
#     pass  # No need to close onboard

alpha_keys = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '⌫'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '⏎'],
    ['⇪', 'z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ["?123", '.', ',', '?', '!', '@', '#', '$', '%', '&'],
    ['␣']
]

shift_keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '⌫'],
    ['~', '@', '#', '$', '%', '^', '&', '*', '(',')','⏎'],
    ['⇪', '+', '=', '/', '-', '\\', '|', '`', '"', "'"],
    ['Abc', '[', ']', '{', '}', '<', '>', ':', ';', '!', '?'],
    ['␣']
]

geometry = '800x400'
root = tk.Tk()
root.title("On-screen Keyboard")
root.geometry(geometry)

create_keyboard(root)
update_keys()

root.mainloop()


# but i am runing this code in my terminal and trying to use this keyboard on my browser its not working why ? 
# any changes i need take or not please tell me...


