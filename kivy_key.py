#!/usr/bin/python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class VirtualKeyboard(GridLayout):
    def __init__(self, **kwargs):
        super(VirtualKeyboard, self).__init__(**kwargs)
        self.cols = 10  # Adjust the number of columns for your resolution
        self.create_keyboard()

    def create_keyboard(self):
        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'
        ]
        for key in keys:
            button = Button(text=key)
            button.bind(on_press=self.on_key_press)
            self.add_widget(button)

    def on_key_press(self, instance):
        print('Key pressed:', instance.text)

class VirtualKeyboardApp(App):
    def build(self):
        return VirtualKeyboard()

if __name__ == '__main__':
    VirtualKeyboardApp().run()

