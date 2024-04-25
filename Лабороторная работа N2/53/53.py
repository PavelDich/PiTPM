import math

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def get_s(self):
        return math.pi * (self.radius ** 2)
    
    def get_p(self):
        return 2 * math.pi * self.radius