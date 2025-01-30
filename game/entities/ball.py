from kivy.uix.image import Image
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Ball(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    base_speed = NumericProperty(8)

    def reset(self):
        self.velocity = Vector(0, -self.base_speed)
