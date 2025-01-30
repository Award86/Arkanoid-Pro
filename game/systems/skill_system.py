from kivy.properties import DictProperty, NumericProperty

class SkillSystem:
    xp = NumericProperty(0)
    level = NumericProperty(1)
    skill_tree = DictProperty({
        'paddle_size': {'level': 0, 'max': 5, 'xp_cost': 100},
        'ball_speed': {'level': 0, 'max': 3, 'xp_cost': 150},
        'magnet': {'level': 0, 'max': 2, 'xp_cost': 200}
    })
    
    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.required_xp:
            self.level_up()
            
    @property
    def required_xp(self):
        return self.level * 500 + 1000
            
    def level_up(self):
        self.level += 1
        self.xp -= self.required_xp
        # Розблокування нових можливостей
