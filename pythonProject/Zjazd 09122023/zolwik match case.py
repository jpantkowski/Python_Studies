"""
Zaimplementuj klasę Turtle
atrybut: x, y, direction
metody:
forward
backward
left
right
Początkowy stan:
self.x = 0
self.y = 0
self.direction = "up"
"""
class Turtle: #Tank controls
    def __init__(self, x = 0, y = 0, direction = "up"):
        self.x = x
        self.y = y
        self.direction = direction

    def right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        else:
            self.direction = "up"

    def left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        else:
            self.direction = "up"

    def forward(self, move = 0):
        if self.direction == "up":
            self.y += move
        elif self.direction == "right":
            self.x += move
        elif self.direction == "down":
            self.y -= move
        else:
            self.x -= move

    def backward(self, move = 0):
        if self.direction == "up":
            self.y -= move
        elif self.direction == "right":
            self.x -= move
        elif self.direction == "down":
            self.y += move
        else:
            self.x += move

zolwik = Turtle()
zolwik.forward(3)
zolwik.right()
zolwik.forward(2)
zolwik.right()
zolwik.backward(1)

import matplotlib.pyplot as plt

points = [(0, 0), (0, 1), (2, 1), (2, 3)]
print(list(zip(*points)))

plt.scatter(*zip(*points))
plt.plot(*zip(*points))
plt.show()

class Ant: #Simplified controls
    def __init__(self, x = 0, y = 0, direction = "up"):
        self.x = x
        self.y = y
        self.direction = direction

    def up(self, move = 0):
        self.y += move

    def down(self, move = 0):
        self.y -= move

    def right(self, move = 0):
        self.x += move

    def left(self, move = 0):
        self.x -= move