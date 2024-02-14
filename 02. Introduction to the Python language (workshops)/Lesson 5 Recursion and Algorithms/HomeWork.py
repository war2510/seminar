print("\033[H\033[J")  # Очистка консоли

# Задание 1
"""
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.
a = 2; b = 3 -> 8
"""


def f(a, b):
    if b == 1:
        return a
    if b == 0:
        return 1
    return f(a, b - 1) * a


a = 5
b = 4
print(f(a, b))  # 625

# Задание 2
"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.
"""


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


a = 3
b = 5
print(sum(max(a, b), min(a, b)))  # 8
