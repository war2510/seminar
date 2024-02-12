import random

print("\033[H\033[J")  # Очистка консоли

"""
Найти n-ое число Фибоначчи через рекурсию
"""


def f(n):
	if n == 0 or n == 1:
		return 1
	return f(n - 1) + f(n - 2)


# n = int(input("Введите n: "))
num = 5

print(f"{num}-ое число Фибоначчи = {f(num)}")


"""
Найти факториал n через рекурсию
"""


def f(n):

	if n <= 0:
		return 1
	return n * f(n - 1)


# n = int(input("Введите n: "))
num = 4

print(f"Факториал {num} = {f(num)}")


"""
В списке заменить максимальное число на минимальное
2 1 1 2 3 5 => 2 1 1 2 3 1
"""


def change(list1):
	max_N = max(list1)
	min_N = min(list1)
	for i in range(num):
		if list1[i] == max_N:
			list1[i] = min_N
	return list1


# n = int(input("Введите n: "))
num = 8

list1 = list()
for i in range(num):
	x = random.randint(1, 5)
	list1.append(x)

print(list1, end=" => ")
print(change(list1))


"""
Напишите функцию, которая с помощью рекурсии определяет, является ли введенное число простым
"""


def simple(n, d=2):
	if d * d > n:
		return True
	if n % d == 0:
		return False
	return simple(n, d + 1)


# def simple(n):
#	 for i in range(2, n):
#		 if not n % i:
#			 return "no"
#	 return "yes"


num = int(input("Введите n: "))
print(simple(num))


"""
Дано натуральное число n и последовательность из n элементов
Надо вывести эту последовательность в обратном порядке
"""


def f(n):
	if n == 0:
		return ""
	k = int(input("Введите число: "))
	return f(n - 1) + f" {k}"


num = int(input("Введите n: "))
print(f(num))
