# print("\033[H\033[J")  # Очистка консоли

"""
найти палиндром через рекурсию
"""


def f(arr, n):
    if n == 0:
        return True
    if arr[n] != arr[-(n + 1)]:
        return False
    return f(arr, n - 1)


s = "1 2 3 3 2 1"
list1 = s.split()

print(f(list1, len(list1) // 2))


# Второй вариант
def pallindrom(stroka):
    if len(stroka) <= 1:
        return True
    if stroka[0] != stroka[-1]:
        return False
    return pallindrom(stroka[1:-1])


print(pallindrom("qwewq"))

print("\n")

"""
Дружественные числа.
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
"""

n = 300


# Сумма делителей
def sum_of_dividors(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s


# Первый вариант
kor = []
for i in range(1, n + 1):
    kor.append(tuple([i, sum_of_dividors(i)]))

for i in range(len(kor)):
    for j in range(i + 1, len(kor)):
        if kor[i][0] == kor[j][1] and kor[i][1] == kor[j][0]:
            print(*kor[i])


# Второй вариант
for i in range(1, n + 1):
    j = sum_of_dividors(i)
    if i < j <= n and i == sum_of_dividors(j):
        print(i, j)


# Третий вариант
kor = {}
for i in range(1, n + 1):
    kor[i] = sum_of_dividors(i)

for i in range(1, n + 1):
    if kor[i] in kor and kor[kor[i]] == i and i < kor[i]:
        print(i, kor[i])


print("\n")

"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
(необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Sample Output:
1 2 7 8
"""
list1 = [
    "osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen",
    "anton",
    "aoooooooooontooooo",
    "elelelelelelelelelel",
    "ntoneeee",
    "tonee",
    "253235235a5323352n25235352t253523523235oo235523523523n",
    "antoooooooooooooooooooooooooooooooooooooooooooooooooooon",
    "unton",
]
find_str = "anton"


# Вариант 1 строка
count = 0

for i in range(len(list1)):
    for character in list1[i].lower():
        if character == find_str[count]:
            count += 1
            if count == 5:
                print(i + 1, end=" ")
                break
    count = 0
print()


# Вариант 2 словарь
count = 0
# dict = {0: "a", 1: "n", 2: "t", 3: "o", 4: "n"}
dict = {i: find_str[i] for i in range(len(find_str))}

for i in range(len(list1)):
    for character in list1[i].lower():
        if character == dict[count]:
            count += 1
            if count == 5:
                print(i + 1, end=" ")
                break
    count = 0
print()


# Вариант 3 рекурсия
def is_f(str, f):
    if len(f) == 0:
        return True
    if len(str) == 0:
        return False
    if str[-1] == f[-1]:
        return is_f(str[:-1], f[:-1])
    return is_f(str[:-1], f)


for i in range(len(list1)):
    if is_f(list1[i], find_str):
        print(i + 1, end=" ")
