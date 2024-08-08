#!/usr/bin/python3


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KeyboardApp(App):
    def build(self):
        layout = GridLayout(cols=10)
        self.text_input = TextInput(font_size=32, size_hint_y=None, height=100)
        layout.add_widget(self.text_input)

        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/',
            'Space', 'Enter'
        ]

        for key in keys:
            if key == 'Space':
                button = Button(text='Space', size_hint_x=3)
                button.bind(on_press=self.on_key_press)
                layout.add_widget(button)
            else:
                button = Button(text=key)
                button.bind(on_press=self.on_key_press)
                layout.add_widget(button)

        return layout

    def on_key_press(self, instance):
        if instance.text == 'Enter':
            self.text_input.text += '\n'
        elif instance.text == 'Space':
            self.text_input.text += ' '
        else:
            self.text_input.text += instance.text

if __name__ == '__main__':
    KeyboardApp().run()

