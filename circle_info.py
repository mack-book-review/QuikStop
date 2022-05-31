import random

class CircleInfo():
    WIDTH = 500
    HEIGHT = 500
    COLORS = {
        "orange": (245,179,66),
        "blue" : (76,234,237)
    }
    def __init__(self,color = "blue"):
        self.radius = random.randint(10, 50)
        self.centerx = random.randint(self.radius, CircleInfo.WIDTH - self.radius)
        self.centery = random.randint(self.radius, CircleInfo.HEIGHT - self.radius)
        self.center = (self.centerx,self.centery)
        self.color = CircleInfo.COLORS[color]
