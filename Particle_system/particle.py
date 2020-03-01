import random

class Particle:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.x_velocity = 0
        self.y_velocity = 0
    def randomize(self):
        self.x_position = random.randrange(0, 400)
        self.y_position = random.randrange(0, 400)
        self.x_velocity = random.randrange(-5, 5)
        self.y_velocity = random.randrange(-5, 5)
    def move(self):
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity
        if self.x_position > 400 or self.y_position > 400 or self.x_position < 0 or self.y_position < 0:
            self.x_position = random.randrange(0, 400)
            self.y_position = random.randrange(0, 400)

    def draw_it(self):
        print(self.x_position)
        print(self.y_position)
        circle(self.x_position, self.y_position, 10)
