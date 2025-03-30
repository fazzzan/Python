import turtle as t
import signal
import os
import time
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def turtle_param(bgcolor, speed, width, color):
    t.bgcolor(bgcolor)
    t.speed(speed)
    t.pensize(width)
    t.pencolor(color)

def turtle_circle(size, angle, shift):
    turtle_param('black', 'fast', 20, next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    turtle_circle(size + 5, angle + 1, shift + 1)


if __name__ == '__main__':
    turtle_circle(10, 0, 1)

#    while True:
#        print("Countdown to pause")
#        for i in range(10):
#            time.sleep(0.1)
#            print(i)
