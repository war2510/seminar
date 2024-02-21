import sys
from io import StringIO

# Сохраняем оригинальный stdin
original_stdin = sys.stdin

import turtle

# ----------------------------------------------------------------------------
def signature():
    """
    Рисует подпись в правом нижнем углу экрана.
    """
    import os

    text = "Rif.  " + os.path.basename(__file__)
    turtle.penup()
    turtle.setpos(Screen().screensize()[0] - 30, -Screen().screensize()[1] - 20)
    turtle.write(text, move=False, align="right", font=("Arial", 8, "normal"))


def turtlette():
    """
    Рисует спираль из кругов.
    """
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.pensize(1)
    turtle.hideturtle()
    turtle.speed(0)

    for i in range(40, 160):
        turtle.left(8 - 160 // i)
        turtle.circle(i)

    signature()
    turtle.done()


if __name__ == "__main__":
    print("This is a module with some functions for turtle graphics.")
    # turtlette()

# ----------------------------------------------------------------------------
input_data = "400\n200"
sys.stdin = StringIO(input_data)


def rectangle(width, height):
    """
    Рисует прямоугольник заданной ширины и высоты.

    Args:
        width (int): Ширина прямоугольника.
        height (int): Высота прямоугольника.
    """
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.done()


# rectangle(int(input()), int(input()))

sys.stdin = original_stdin

# ----------------------------------------------------------------------------
input_data = "200"
sys.stdin = StringIO(input_data)


def triangle(side):
    """
    Рисует правильный треугольник заданной длины стороны.

    Args:
        side (int): Длина стороны треугольника.
    """
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
        turtle.done()


# triangle(int(input()))

sys.stdin = original_stdin


# ----------------------------------------------------------------------------
input_data = "200"
sys.stdin = StringIO(input_data)
n = 16
g = 45


def square(side):
    """
    Рисует фигуру, состоящую из трех квадратов.

    Args:
        side (int): Длина стороны квадрата.
    """
    for _ in range(n):
        turtle.left(g)
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
            turtle.done()


square(int(input()))

sys.stdin = original_stdin

# ----------------------------------------------------------------------------

import random

turtle.speed(0)
turtle.pencolor("white")
for i in range(60):
    turtle.fillcolor(
        random.randrange(256), random.randrange(200), random.randrange(200)
    )
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(80 - i)
        turtle.left(60)
        turtle.forward(90 - i)
        turtle.left(120)
    turtle.end_fill()
    turtle.left(21)
turtle.done()

# ----------------------------------------------------------------------------

def sneg(size):
    """
    Рисует снежинку заданного размера.

    Args:
        size (int): Размер снежинки.
    """
    for i in ["red", "yellow", "green", "orange", "blue", "purple"] * 2:
        turtle.color(i)
        turtle.forward(size)
        turtle.left(180)
        turtle.forward(size)
        turtle.left(30)
    turtle.done()


sneg(120)

# ----------------------------------------------------------------------------

def cccp(size):
    """
    Рисует красную звезду заданного размера.

    Args:
        size (int): Размер звезды.
    """
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.done()


turtle.pensize(5)
turtle.color("red")
cccp(200)

# ----------------------------------------------------------------------------

import turtle
import datetime

n = 12

turtle.Screen().bgcolor("gray")
turtle.shape("turtle")
turtle.pensize(5)

for i in range(n):
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    turtle.forward(15)

    turtle.stamp()
    turtle.backward(150)
    turtle.left(360 / n)

turtle.shape("triangle")


b = datetime.datetime.now()
h, m = b.hour, b.minute
if h > 12:
    h = h - 12

turtle.right(h * 30 - 90 + m / 2)
turtle.pendown()
turtle.forward(60)
turtle.stamp()
turtle.backward(60)
turtle.home()
turtle.right(m * 6 - 90)
turtle.forward(90)
turtle.stamp()
turtle.shape("turtle")
turtle.backward(90)


turtle.stamp()

# ----------------------------------------------------------------------------

colors = ["red", "blue", "yellow", "green", "purple", "orange"]
s = 1
n = 5
for i in range(8):
    for j in colors:
        turtle.pensize(s)
        turtle.pencolor(j)
        turtle.forward(n)
        turtle.left(45)
        n += 2
    s += 2
