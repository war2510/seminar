import sys
from io import StringIO
from random import *
import string

# Сохраняем оригинальный stdin
original_stdin = sys.stdin

"""
Напишите программу, которая с помощью модуля random генерирует случайный пароль.
Программа принимает на вход длину пароля и выводит случайный пароль,
содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.
Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.
"""

# Заранее заданные значения, которые должны быть "введены"
input_data = "5"
# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)


length = int(input())  # длина пароля

password = ""
for i in range(length):
    if randint(0, 1):
        password += chr(randint(65, 90))
    else:
        password += chr(randint(97, 122))
print(password)

print()
# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin

"""
Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.
Примечание. Убедитесь, что сгенерированные числа не содержат дубликатов.
"""
numbers = set()
while len(numbers) < 7:
    numbers.add(randint(1, 49))


print(*sorted(numbers))
print()

"""
IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.
Напишите функцию, которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
"""


def generate_ip():
    s = [randint(0, 255) for _ in range(4)]
    return ".".join([str(i) for i in s])


print(generate_ip())
print()

"""
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter
где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.
"""


def generate_index():
    num = [randint(0, 99) for _ in range(2)]
    let = [choice(string.ascii_uppercase) for _ in range(4)]
    return f"{let[0]}{let[1]}{num[0]}_{num[1]}{let[2]}{let[3]}"


print(generate_index())
print()


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

shuffle(matrix)
print(matrix)
print()

"""
Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
номер не может начинаться с нулей; номер лотерейного билета должен состоять из 7 цифр;
все 100 лотерейных билетов должны быть различными.
"""
num = set()
while len(num) < 10:
    num.add(randint(1000000, 9999999))

print(*num, sep="\n")
print()

"""
Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.
"""

# Заранее заданные значения, которые должны быть "введены"
input_data = "программу"
# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)

s = list(input())
shuffle(s)
print("".join(s))
print()

# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin

"""
Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75
(включительно), при этом центральная клетка является пустой (она заполняется числом 0).
Для наглядности рекомендуем отводить на вывод каждого числа ровно 3 символа.
Для этого используйте строковый метод ljust().
"""

list1 = [i for i in range(1, 76)]
num = sample(list1, 24)

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            print(str(0).ljust(3), end="")
        else:
            print(str(num.pop()).ljust(3), end="")
    print()
print()

"""
На вход программе в первой строке подается число n – общее количество учеников.
Далее идут n строк, содержащих имена и фамилии учеников.
вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга, разделённые дефисом
"""

# Заранее заданные значения, которые должны быть "введены"
input_data = "\n".join(
    [
        "5",
        "Владимир Смолов",
        "Тагир Хан",
        "Давид Лавров",
        "Арина Приходько",
        "Глеб Анисимов",
    ]
)
# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)

list1 = [input() for _ in range(int(input()))]
shuffle(list1)
for i in range(len(list1)):
    print(f"{list1[i - 1]} - {list1[i]}")

print()

# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin

"""
Генератор паролей 1
генерирует n паролей длиной m символов, состоящих из строчных и прописных английских букв и цифр,
кроме тех, которые легко перепутать между собой: "lI1oO0"
в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
"""
# Заранее заданные значения, которые должны быть "введены"
input_data = "\n".join(["5", "10"])

# Подменяем stdin на StringIO объект с заранее заданными значениями
sys.stdin = StringIO(input_data)

# Список допустимых символов для пароля, исключая путающие символы
allowed_chars = "".join(
    (set(string.ascii_letters) | set(string.digits)) - set("lI1oO0")
)


def generate_passwords(count, length):
    for _ in range(count):
        while True:
            passw = choices(allowed_chars, k=length)
            if (
                any(c in string.ascii_lowercase for c in passw)
                and any(c in string.ascii_uppercase for c in passw)
                and any(c in string.digits for c in passw)
            ):
                print("".join(passw))
                break


generate_passwords(int(input()), int(input()))
print()

# Возвращаем оригинальный stdin обратно на место
sys.stdin = original_stdin

"""
Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств
"""
n = 10**6  # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)

    if -2 <= x <= 2 and -2 <= y <= 2 and x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:
        k += 1

print((k / n) * s0)
print()

"""
Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа π.
"""
n = 10**6  # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if x**2 + y**2 <= 1:
        k += 1

print((k / n) * s0)
print()

# визуализация (один из вариантов решения) через библиотеку matplotlib.pyplot:
import numpy as np
import matplotlib.pyplot as plt

n = 1e3
x = 1 - 2 * np.random.random(int(n))
y = 1 - 2.0 * np.random.random(int(n))
insideX, insideY = x[(x**2 + y**2) <= 1], y[(x**2 + y**2) <= 1]
outsideX, outsideY = x[(x**2 + y**2) > 1], y[(x**2 + y**2) > 1]

fig, ax = plt.subplots(1)
ax.scatter(insideX, insideY, c="b", alpha=0.8, edgecolor=None)
ax.scatter(outsideX, outsideY, c="r", alpha=0.8, edgecolor=None)
ax.set_aspect("equal")
# fig.show()  # В Jupyter Notebook не требуется, иначе разкомментируйте

print((len(insideX) / n) * 4)


import time


def is_sort(nums):  # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        shuffle(nums)
    return nums


numbers = list(range(12))
shuffle(numbers)  # перемешиваем начальный список
print("Начальный список:", numbers)  # выводим начальный список

start_time = time.time()  # Запоминаем время начала сортировки
sorted_numbers = bogosort(numbers)  # Сортируем числа
end_time = time.time()  # Запоминаем время окончания сортировки

print("Отсортированный список:", sorted_numbers)  # Выводим отсортированный список
print(
    "Время выполнения сортировки: {:.2f} секунд".format(end_time - start_time)
)  # Выводим время выполнения сортировки

print()
