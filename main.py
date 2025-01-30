from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from game.ui.screens import MainMenuScreen, GameScreen

class ArkanoidApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    ArkanoidApp().run()
