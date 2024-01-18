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
class Turtle:
    def __init__(self, x: int = 0, y: int = 0, direction = "up"):
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
        elif self.direction == "left":
            self.direction = "up"
        return self.direction

    def left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "up"
        return self.direction


    def forward(self, move = 0):
        if self.direction == "up":
            self.y += move
        elif self.direction == "right":
            self.x += move
        elif self.direction == "down":
            self.y -= move
        elif self.direction == "left":
            self.x -= move
        return self.x, self.y

    def backward(self, move = 0):
        if self.direction == "up":
            self.y -= move
        elif self.direction == "right":
            self.x -= move
        elif self.direction == "down":
            self.y += move
        elif self.direction == "left":
            self.x += move
        return self.x, self.y

zolwik = Turtle()

def my_custom_turtle_path(turtle):
    points = [(0, 0)]
    points.append(turtle.forward(3))
    turtle.right()
    points.append(turtle.forward(2))
    turtle.right()
    points.append(turtle.backward(1))
    print(turtle.x, turtle.y)

import matplotlib.pyplot as plt

points = [(0, 0), (0, 1), (2, 1), (2, 3)]
print(list(zip(*points)))

plt.scatter(*zip(*points))
plt.plot(*zip(*points))
plt.show()

my_custom_turtle_path(zolwik)