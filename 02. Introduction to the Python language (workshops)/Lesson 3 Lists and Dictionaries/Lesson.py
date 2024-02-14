print("\033[H\033[J")  # Очистка консоли

"""
Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

arr = [1, 1, 2, 0, -1, 3, 4, 4]
arr_un = []

for i in arr:
    if i not in arr_un:
        arr_un.append(i)
print(len(arr_un))
print()

"""
Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
arr = [1, 2, 3, 4, 5]
k = 3
print(arr)

k = k % len(arr)
arr_un = arr[k - 1 :] + arr[: k - 1]
print(arr_un)


# Второй вариант решения
def move(lst, steps):
    if steps > 0:
        for i in range(steps):
            lst.insert(0, lst.pop())


move(arr, k)
print(arr)
print()

"""
Задача №21. Решение в группах Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

dic = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": " S005 "},
    {" V ": " S009 "},
    {" VIII ": " S007 "},
]

s = set()
for i in dic:
    for k, v in i.items():
        s.add(v)
print(sorted(s))

# Второй вариант решения
s = set()
for i in dic:
    for v in i.values():
        s.add(v)
print(sorted(s))

# Третий вариант решения
s = set()

for i in dic:
    for j in i:
        s.add(i[j])
print(sorted(s))
print()

"""
Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:

print(*sorted(d.items()))

Sample Input:
+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
Sample Output:
('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])
"""
dic = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"
dic = dic.split()
d = {}

for i in dic:
    key = i[:2]
    val = i
    try:
        d[key].append(val)
    except KeyError:
        d[key] = [val]

print(*sorted(d.items()))
