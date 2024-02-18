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
input_data = "\n".join(
    [
        "0.1244354689",
        "-12.1224",
    ]
)
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
