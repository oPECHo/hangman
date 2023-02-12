import kivy
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class ButtonsLayout(GridLayout):
    INSTANCES = []

    def __init__(self, **kwargs):
        super(ButtonsLayout, self).__init__(**kwargs)
        ButtonsLayout.INSTANCES.append(self)
        self.rows = 2
        self.cols = 13
        self.buttons = {}
        self.create_buttons()

    def create_buttons(self):
        for alphabet in string.ascii_uppercase:
            button = Button(
                text=alphabet,
                font_name="fonts/Plaguard.otf",
                font_size=24,
            )
            self.add_widget(button)
            self.buttons[alphabet] = button
            
class MyRoot(BoxLayout):
    pass
