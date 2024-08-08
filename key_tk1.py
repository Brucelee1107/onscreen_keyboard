import tkinter as tk
from pynput.keyboard import Controller, Key

keyboard = Controller()

caps_lock = False
shift = False
console_output = ""

# Function for key event
def on_key_press(key):
    global caps_lock, shift, console_output
    if key == '⌫': 
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    elif key == '⇪': 
        global caps_lock
        caps_lock = not caps_lock
        update_keys()
    elif key == '␣': 
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif key == '⏎':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif key == "?123" or key == "Abc":
        global shift 
        shift = not shift
        create_keyboard(root)
    else:
        if shift and key.isalpha():
            key = key.upper()
        elif caps_lock and key.isalpha():
            key = key.upper()
        keyboard.press(key)
        keyboard.release(key)
    print(console_output, end='\r') 


# Function for updating the keys
def update_keys():
    for button, key in zip(key_buttons, [key for row in (shift_keys if shift else alpha_keys) for key in row]):
        if key == '⇪': 
            button.config(bg='yellow' if caps_lock else 'grey')
        elif key == "?123" or key == "Abc":
            button.config(bg='yellow' if shift else 'grey')
        else:
            button.config(text=key.upper() if (caps_lock or shift) and key.isalpha() else key) 
            root.update()

# Function for creating the keyboard
def create_keyboard(root):
    global key_buttons
    key_buttons = []

    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

    # loop for creating keys 
    for row in (shift_keys if shift else alpha_keys): 
        key_row = tk.Frame(root)
        key_row.pack(expand=True, fill='both')
        for key in row:
            button = tk.Button(key_row, text=key, command=lambda k=key: on_key_press(k))
            button.pack(side='left', expand=True, fill='both')
            key_buttons.append(button)

    update_keys()

# Alphabetic keys
alpha_keys = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '⌫'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '⏎'],
    ['⇪', 'z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ["?123", '.', ',', '?', '!', '@', '#', '$', '%', '&'],
    ['␣']
]

# Numeric and Special characters
shift_keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '⌫'],
    ['-', '/', ':', ';', '(', ')', '$', '&', '@', '"', '⏎'],
    ['⇪', '+', '=', '*', '_', '\\', '|', '~', "'"],
    ['Abc', '[', ']', '{', '}', '<', '>', '^', '!', '?'],
    ['␣']
]

geometry = '400x200' # keyboard resolution adjustable
root = tk.Tk()
root.title("On-screen Keyboard") 
root.geometry(geometry)

create_keyboard(root)
update_keys()
root.mainloop()
