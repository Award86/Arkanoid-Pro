from kivy.vector import Vector

class PhysicsEngine:
    GRAVITY = Vector(0, -0.98)
    
    def __init__(self):
        self.objects = []
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def update_objects(self, dt):
        for obj in self.objects:
            obj.velocity += self.GRAVITY * dt
            obj.pos += obj.velocity * dt
            self.check_boundaries(obj)
            
    def check_boundaries(self, obj):
        if obj.right > obj.parent.width:
            obj.right = obj.parent.width
            obj.velocity.x *= -0.8
