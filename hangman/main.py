import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyRoot(BoxLayout):
    pass

class Hangman(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    Hangman().run()
