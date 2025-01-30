from kivy.uix.image import Image
from kivy.properties import NumericProperty

class Paddle(Image):
    speed = NumericProperty(10)
    size_multiplier = NumericProperty(1.0)

    def move_left(self):
        self.x = max(0, self.x - self.speed)

    def move_right(self, max_width):
        self.right = min(max_width, self.right + self.speed)
