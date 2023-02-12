import kivy
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

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
    HANGMAN_IMG = StringProperty()
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.start_game()
    def start_game(self):
        self.HANGMAN_IMG = "images/hangman0.png"


class Hangman(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    Hangman().run()
