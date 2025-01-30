from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
#:include ui/game_screen.kv
#:include ui/main_menu.kv
#:include ui/shop_screen.kv
''')

class GameScreen(Screen):
    def on_enter(self):
        self.engine = self.manager.engine
        
class MainMenu(Screen):
    pass

class ShopScreen(Screen):
    def update_balance(self):
        self.ids.coin_label.text = f"Coins: {self.manager.engine.player_coins}"
