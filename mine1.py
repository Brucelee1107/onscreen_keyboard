#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class KeyboardApp(App):
    def build(self):
        layout = GridLayout(cols=10, spacing=5, padding=10)

        # Add keys here
        keys = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':',
                'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?']

        for key in keys:
            button = Button(text=key, font_size=10)
            button.bind(on_press=self.on_key_press)
            layout.add_widget(button)

        return layout

    def on_key_press(self, instance): 
        print(instance.text)

if __name__ == '__main__':
    KeyboardApp().run()
