from kivy.uix.image import Image
from kivy.properties import NumericProperty, ListProperty

class Brick(Image):
    BRICK_TYPES = {
        'normal': {'health': 1, 'color': [1,0,0,1], 'score': 50},
        'armored': {'health': 3, 'color': [0.5,0.5,0.5,1], 'score': 150},
        'explosive': {'health': 1, 'color': [1,0.5,0,1], 'score': 200}
    }
    
    health = NumericProperty(1)
    brick_type = 'normal'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_type(self.brick_type)
        
    def set_type(self, brick_type):
        self.brick_type = brick_type
        props = self.BRICK_TYPES[brick_type]
        self.health = props['health']
        self.color = props['color']
