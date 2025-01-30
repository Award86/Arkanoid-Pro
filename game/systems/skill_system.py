from kivy.properties import DictProperty, NumericProperty

class SkillSystem:
    xp = NumericProperty(0)
    level = NumericProperty(1)
    skills = DictProperty({
        'paddle_size': {'current': 0, 'max': 5, 'cost': 100},
        'ball_speed': {'current': 0, 'max': 3, 'cost': 150},
        'extra_life': {'current': 0, 'max': 2, 'cost': 200}
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
