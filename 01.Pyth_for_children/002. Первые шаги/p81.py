import turtle
import turtle as t
import signal
import os
import time
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def rectangle(horizontal, vertical, color):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
#    t.left(90)
#    t.forward(50)

def arm(color):
    # руки
#    t.penup()
#    t.goto(-150, 70)
#    rectangle(60, 15, "grey")
#    t.penup()
#    t.goto(-150, 110)
#    rectangle(15, 40, "grey")

#    t.penup()
#    t.goto(10, 70)
#    rectangle(60, 15, "grey")
#    t.penup()
#    t.goto(55, 110)
#    rectangle(15, 40, "grey")

    t.pendown()
    t.begin_fill()
    t.color(color)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ступни
    t.penup()
    t.goto(-100, -150)
    rectangle(50, 20, "blue")
    t.penup()
    t.goto(-30, -150)
    rectangle(50, 20, "blue")
    # Ноги
    t.penup()
    t.goto(-25, -50)
    rectangle(15, 100, "grey")
    t.penup()
    t.goto(-55, -50)
    rectangle(-15, 100, "grey")
    # Туловище
    t.penup()
    t.goto(-90, 100)
    rectangle(100, 150, "red")

    # руки
#    t.goto(-90, 85)
#    t.setheading(180)
#    arm('light blue')

#    t.goto(-90, 20)
#    t.setheading(180)
#    arm('purple')

#    t.goto(10, 85)
#    t.setheading(0)
#    arm('goldenrod')

    t.goto(-90, 80)
    t.setheading(135)
    arm('light blue')
    t.goto(10, 80)
    t.setheading(315)
    arm('light blue')


    # шея
    t.penup()
    t.goto(-50, 120)
    rectangle(15, 20, "grey")

    # глова
    t.penup()
    t.goto(-85, 170)
    rectangle(80, 50, "red")

    # глаза
    t.penup()
    t.goto(-60, 160)
    rectangle(30, 10, "white")
    t.penup()
    t.goto(-55, 155)
    rectangle(5, 5, "black")
    t.goto(-40, 155)
    rectangle(5, 5, "black")

    # рот
    t.penup()
    t.goto(-65, 135)
    rectangle(40, 5, "black")

    t.hideturtle()
    PID = os.getpid()

    while True:
        print("Countdown to pause")
        for i in range(10):
            time.sleep(0.1)
            print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
