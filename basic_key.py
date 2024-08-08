import pyglet
from pyglet.window import mouse
import pyautogui

# Define the window
window = pyglet.window.Window(800, 600, "Onscreen Keyboard")

# Define the button class 
class Button:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (200, 200, 200)
        self.label_obj = pyglet.text.Label(
            label,
            font_name='Arial',
            font_size=18,
            x=x + width // 2,
            y=y + height // 2,
            anchor_x='center',
            anchor_y='center'
        )

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
            ('v2f', [self.x, self.y, 
                     self.x + self.width, self.y, 
                     self.x + self.width, self.y + self.height, 
                     self.x, self.y + self.height]),
            ('c3B', self.color * 4)
        )
        self.label_obj.draw()

    def on_click(self):
        pyautogui.write(self.label)

# Define the keyboard buttons
buttons = [
    Button('A', 50, 400, 50, 50),
    Button('B', 120, 400, 50, 50),
    Button('C', 190, 400, 50, 50),
    # Add more buttons as needed
]

@window.event
def on_draw():
    window.clear()
    for button in buttons:
        button.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        for btn in buttons:
            if btn.x <= x <= btn.x + btn.width and btn.y <= y <= btn.y + btn.height:
                btn.on_click()

pyglet.app.run()
