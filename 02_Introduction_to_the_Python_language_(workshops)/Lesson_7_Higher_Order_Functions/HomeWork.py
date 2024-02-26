print("\033[H\033[J")  # Очистка консоли

# Задание 1
"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
Между элементами должен быть 1 пробел, в конце строки пробел не нужен.
"""


def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    for i in range(1, num_rows + 1):
        rows = []
        for j in range(1, num_columns + 1):
            rows.append(operation(i, j))
        print(*rows)


print_operation_table(lambda x, y: x * y, 9, 9)

# Задание 2
"""
Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!
"""
stroka = "пара-ра-рам рам-пам-папам па-ра-па-дам"


def ritm(phrase):
    count_vowels = [
        sum(1 for char in phrases.lower() if char in "аеёиоуыэюя")
        for phrases in phrase.split()
    ]
    if len(count_vowels) < 2:
        return "Количество фраз должно быть больше одной!"
    elif len(set(count_vowels)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"


print(ritm(stroka))

# Саиджалол Содиков (recursion)
slova = stroka.split()
kolvo_slogov = list()


def check(list_str):
    if len(list_str) <= 0:
        return True
    if list_str[0] == list_str[1]:
        return check(list_str[1:])
    return False


if len(slova) <= 1:
    print("Количество фраз должно быть больше одной!")
else:
    for i in slova:
        slogi_v_slove = 0
        for j in i:
            if j in "ёуеэоаыяию":
                slogi_v_slove += 1
        kolvo_slogov.append(slogi_v_slove)
    if check(kolvo_slogov):
        print("Парам пам-пам")
    else:
        print("Пам парам")
