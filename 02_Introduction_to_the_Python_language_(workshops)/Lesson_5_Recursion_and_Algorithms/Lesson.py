import random

print("\033[H\033[J")  # Очистка консоли

"""
Найти n-ое число Фибоначчи через рекурсию
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num = 5

print(f"{num}-ое число Фибоначчи = {fibonacci(num)}\n")


"""
Найти факториал n через рекурсию
"""


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


num = 5

print(f"Факториал {num} = {factorial(num)}\n")


"""
В списке заменить максимальное число на минимальное
2 1 1 2 3 5 => 2 1 1 2 3 1
"""


def change_max_to_min(list1):
    max_N = max(list1)
    min_N = min(list1)
    for i in range(len(list1)):
        if list1[i] == max_N:
            list1[i] = min_N
    return list1


print("В списке заменить максимальное число на минимальное")
num = 8

list1 = [random.randint(1, 5) for i in range(num)]

print(list1, end=" => ")
print(change_max_to_min(list1))
print()


"""
Напишите функцию, которая с помощью рекурсии определяет, является ли введенное число простым
"""


def is_prime(n, d=2):
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)


num = int(input("Введите n: "))
print(f"Это число является простым: {is_prime(num)}\n")
print()


"""
Дано натуральное число n и последовательность из n элементов
Надо вывести эту последовательность в обратном порядке
"""


def f(arr, n):
    if n == 0:
        return ""
    return f" {arr[n - 1]}" + f(arr, n - 1)


print("Надо вывести список в обратном порядке")
num = int(input("Введите длину списка: "))
list1 = [random.randint(0, 9) for i in range(num)]
print(list1, end=" => ")

print(f(list1, num))
