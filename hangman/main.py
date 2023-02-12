import kivy
import string
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from words import WORDS

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
    ERRORS = StringProperty()
    HANGMAN_IMG = StringProperty()
    GAME_MSG = StringProperty()
    WORD_DISPLAY = StringProperty()
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.RANDOM_WORD = ""
        self.button_layout = ButtonsLayout.INSTANCES[0]
        self.start_game()
    def start_game(self):
        self.RANDOM_WORD = random.choice(WORDS)
        self.ERRORS = "0"
        self.HANGMAN_IMG = "images/hangman0.png"
        self.GAME_MSG = "Guess the word"
        self.WORD_DISPLAY = " ".join(["_" for _ in self.RANDOM_WORD])


class Hangman(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    Hangman().run()
