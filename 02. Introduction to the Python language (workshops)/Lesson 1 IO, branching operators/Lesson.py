print("\033[H\033[J") # Очистка консоли

"""
Задача №1.
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
"""

n = 700
m = 750

print(abs(-m // n))  # остаток цельночисленного деления округляется до меньшего целого
print(((m + n - 1) // n))
print((m // n) + 1 - (m == n))


"""Задача №3.
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
"""
a = 20
b = 21
c = 22

s = (a // 2 + (a % 2 != 0)) + (abs(-b // 2)) + ((c + 1) // 2)  # три варианта решения

print(s)

"""
Вводится три длины сторон треугольника. Определить можно ли из них построить треугольник
Сумма двух сторон должна быть больше третей
"""

a = 3
b = 4
c = 5


if a + b > c and b + c > a and a + c > b:
	print("Yes")
else:
	print("No")
