import turtle as t
from random import randint, random

size = 300
points = 11


def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(0)
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

if __name__ == '__main__':
    t.Screen().bgcolor('dark blue')
    while True:
        ranPts = randint(2, 7) * 2 + 1
        ranSize = randint(10, 50)
        ranCol = (random(), random(), random())
        ranX = randint(-350, 300)
        ranY = randint(-250, 250)
        draw_star(ranPts, ranSize, ranCol, ranX, ranY)
