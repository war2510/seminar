import sys
from io import StringIO

# Сохраняем оригинальный stdin
original_stdin = sys.stdin

from turtle import *


def signature():
    import os

    text = "Rif.  " + os.path.basename(__file__)
    penup()
    setpos(Screen().screensize()[0] - 30, -Screen().screensize()[1] - 20)
    write(text, move=False, align="right", font=("Arial", 8, "normal"))


def turtlette():
    bgcolor("black")
    pencolor("white")
    pensize(1)
    hideturtle()
    speed(0)

    for i in range(40, 160):
        left(8 - 160 // i)
        circle(i)

    signature()
    done()


if __name__ == "__main__":
    print("This is a module with some functions for turtle graphics.")
    # turtlette()


"""
Напишите программу, которая рисует прямоугольник.
Программу нужно оформить в виде функции rectangle(width, height), где width, height – ширина и высота прямоугольника.
"""
input_data = "400\n200"
sys.stdin = StringIO(input_data)


def rectangle(width, height):
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    done()


# rectangle(int(input()), int(input()))

sys.stdin = original_stdin


"""
Напишите программу, которая рисует правильный треугольник.
Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.
Величина каждого угла правильного треугольника равна 60 градусам
"""
input_data = "200"
sys.stdin = StringIO(input_data)


def triangle(side):
    for _ in range(3):
        forward(side)
        left(120)
    done()


# triangle(int(input()))

sys.stdin = original_stdin

"""
Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
Напишите функцию square(side), где side – длина стороны квадрата в пикселях.
"""
input_data = "200"
sys.stdin = StringIO(input_data)


def square(side):
    for _ in range(16):
        left(22.5)
        for _ in range(4):
            forward(side)
            left(90)
    done()


square(int(input()))

sys.stdin = original_stdin
