from decimal import *
import sys
from io import StringIO


# Сохраняем оригинальный stdin
original_stdin = sys.stdin


"""
вывел на первой строке сумму всех чисел, а на второй строке
5 самых больших чисел в порядке убывания, разделенных символом пробела.
"""

s = "0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50"
num = [Decimal(i) for i in s.split()]
print(sum(num))
print(*sorted(num, reverse=True)[:5])
print()


"""
вывел сумму наибольшей и наименьшей цифры Decimal числа.
"""
# Заранее заданные значения, которые должны быть "введены"
input_data = "0.1244354689\n-12.1224"
# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)

num = Decimal(input())
str = sorted(list(str(num)))
str = [i for i in str if i.isdigit()]

print(int(str[0]) + int(str[-1]))

# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin

print()

"""
код программы, который вычисляет значение выражения для заданного числа d:
"""
from math import *

# Здесь 'd' - это число типа Decimal, полученное на входе программы
# Для примера возьмем d равным 3
d = Decimal("3")

# Вычисляем значение выражения
# Поскольку модуль math не работает напрямую с Decimal, конвертируем d во float
result = exp(float(d)) + log(float(d)) + log10(float(d)) + sqrt(float(d))

# Выводим результат
print(result)
print()

"""
Десятичные числа хранятся в списке numbers в виде строк.
Дополните приведенный код, чтобы он для каждого десятичного числа вывел его представление в виде обыкновенной дроби в формате:
6.34 = 317/50
4.08 = 102/25
3.04 = 76/25
...
"""
from fractions import *

numbers = ["6.34", "4.08", "3.04", "7.49", "4.45", "5.39", "7.82", "2.76"]
for i in numbers:
    print(f"{i} = {Fraction(i)}")

# [print(f'{i} = {Fraction(i)}') for i in numbers]
print()

"""
Десятичные числа, разделенные символом пробела, хранятся в строковой переменной s.
Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.
"""
s = "0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79"
num = [Fraction(i) for i in s.split()]
print(min(num) + max(num))
print()

"""
Даны два натуральных числа m и n. Напишите программу, которая сокращает дробь n/m и выводит ее
"""
# Заранее заданные значения, которые должны быть "введены"
input_data = "12\n16"
# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)

print(Fraction(int(input()), int(input())))

# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin
print()

"""
Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.
"""
input_data = "2/3\n3/7"
sys.stdin = StringIO(input_data)

a, b = input(), input()
print(f"{a} + {b} = {Fraction(a)+Fraction(b)}")
print(f"{a} - {b} = {Fraction(a)-Fraction(b)}")
print(f"{a} * {b} = {Fraction(a)*Fraction(b)}")
print(f"{a} / {b} = {Fraction(a)/Fraction(b)}")
print()

for op in "+-*/":
    print(f'{a} {op} {b} = {eval(f"Fraction(a){op}Fraction(b)")}')

sys.stdin = original_stdin
print()

"""
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 1/1**2 + 1/2**2 + ... + 1/n**2
"""
input_data = "3"
sys.stdin = StringIO(input_data)

n = int(input())
num = [1 / (Fraction(i) ** 2) for i in range(1, n + 1)]
print(sum(num))

sys.stdin = original_stdin
print()


"""
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения 1/1! + 1/2! + ... + 1/n!
"""
input_data = "3"
sys.stdin = StringIO(input_data)

from math import factorial

n = int(input())
num = [1 / Fraction(factorial(i)) for i in range(1, n + 1)]
print(sum(num))

sys.stdin = original_stdin
print()

"""
На вход программе подается натуральное число n. Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n.
"""
input_data = "23"  # 3/7
sys.stdin = StringIO(input_data)

from math import ceil  # для округления в большую сторону

n = int(input())
num = [Fraction(i, n - i) for i in range(1, ceil(n / 2))]
num = [i for i in num if i.numerator + i.denominator == n]

print(max(num))

sys.stdin = original_stdin
print()

"""
На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания все несократимые дроби,
заключённые между 0 и 1, знаменатель которых не превосходит n.
"""
input_data = "5"  # 1/5 1/4 1/3 2/5 1/2 3/5 2/3 3/4 4/5
sys.stdin = StringIO(input_data)

n = int(input())
num = set()
for i in range(2, n + 1):
    for j in range(1, i):
        num.add(Fraction(j, i))
print(*sorted(num), sep="\n")

# print(*sorted(set(Fraction(j, i) for i in range(2, n + 1) for j in range(1, i))),sep="\n")

sys.stdin = original_stdin
print()
