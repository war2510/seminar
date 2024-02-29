from ast import For

print("\033[H\033[J")  # Очистка консоли

"""
Требуется дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен
"""

emails = {
    "mgu.edu": ["andrei_serov", "alexander_pushkin", "elena_belova", "kirill_stepanov"],
    "gmail.com": ["alena.semyonova", "ivan.polekhin", "marina_abrabova"],
    "msu.edu": ["sergei.zharkov", "julia_lyubimova", "vitaliy.smirnoff"],
    "yandex.ru": ["ekaterina_ivanova", "glebova_nastya"],
    "harvard.edu": ["john.doe", "mark.zuckerberg", "helen_hunt"],
    "mail.ru": ["roman.kolosov", "ilya_gromov", "masha.yashkina"],
}

# Создаем список для хранения всех email-адресов
email_addresses = []

for domain, users in emails.items():
    for user in users:
        email_addresses.append(f"{user}@{domain}")

# Сортируем список email-адресов
email_addresses.sort()

# Выводим отсортированные email-адреса, каждый на новой строке
for email in email_addresses:
    print(email)

print("\n")


"""
Задача 4: Права доступа
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример вывода:
Access denied
OK
OK
OK
OK
"""

rights = {"write": "W", "read": "R", "execute": "X"}
rights_f = ["python.exe X", "book.txt R W", "notebook.exe R W X"]
q_access = [
    "read python.exe",
    "read book.txt",
    "write notebook.exe",
    "execute notebook.exe",
    "write book.txt",
]

# Создание словаря с правами доступа к файлам
dict_rights_f = {}
for entry in rights_f:
    parts = entry.split()
    filename = parts[0]
    file_rights = parts[1:]
    dict_rights_f[filename] = file_rights

# Проверка запросов на доступ
for query in q_access:
    action, filename = query.split()
    if filename in dict_rights_f and rights[action] in dict_rights_f[filename]:
        print("OK")
    else:
        print("Access denied")


print("\n")


"""
Задача 5: Продажи
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.
Программа должна вывести список всех покупателей в лексикографическом порядке, после имени каждого покупателя — двоеточие, затем список названий всех приобретенных им товаров в лексикографическом порядке, после названия каждого товара — количество единиц товара. Информация о каждом товаре выводится на отдельной строке.
Примечание. Обратите внимание на второй тест. Если позиции товаров повторяются, то в итоговый список попадает суммарное количество товара по данной позиции.

Input:
7
Вячеслав Ручка 1
Филипп Ручка 1
Виктория Перо 3
Вячеслав Линейка 4
Виктория Тетрадь 7
Вячеслав Ручка 29
Филипп Циркуль 1
Sample Output 2:

Output:
Виктория:
Перо 3
Тетрадь 7
Вячеслав:
Линейка 4
Ручка 30
Филипп:
Ручка 1
Циркуль 1
"""

purchases = {}

n = int(input())
for _ in range(n):
    parts = input().split()
    name, item, count = parts[0], parts[1], int(parts[2])
    # Создаем вложенный словарь, если он еще не существует, и обновляем количество
    purchases.setdefault(name, {}).setdefault(item, 0)
    purchases[name][item] += count

for name in sorted(purchases):
    print(f"{name}:")
    for item in sorted(purchases[name]):
        print(f"{item} {purchases[name][item]}")
print("\n\n")


"""
Задача 7: Коты и владельцы
Напишите программу, которая выводит имена владельцев котов и их котов.
Игорь Бероев: Муся, 7; Изольда, 2
"""
cats = [
    ("Мартин", 5, "Алексей", "Егоров"),
    ("Фродо", 3, "Анна", "Самохина"),
    ("Вася", 4, "Андрей", "Белов"),
    ("Муся", 7, "Игорь", "Бероев"),
    ("Изольда", 2, "Игорь", "Бероев"),
    ("Снейп", 1, "Марина", "Апраксина"),
    ("Лютик", 4, "Виталий", "Соломин"),
    ("Снежок", 3, "Марина", "Апраксина"),
    ("Марта", 5, "Сергей", "Колесников"),
    ("Буся", 12, "Алена", "Федорова"),
    ("Джонни", 10, "Игорь", "Андропов"),
    ("Мурзик", 1, "Даниил", "Невзоров"),
    ("Барсик", 2, "Виталий", "Соломин"),
    ("Рыжик", 7, "Владимир", "Медведев"),
    ("Матильда", 8, "Андрей", "Белов"),
    ("Гарфилд", 3, "Александр", "Березуев"),
]

owners = {}
for name, age, owner_first, owner_last in cats:
    owner_full_name = f"{owner_first} {owner_last}"
    cat_info = f"{name}, {age}"
    if owner_full_name not in owners:
        owners[owner_full_name] = []
    owners[owner_full_name].append(cat_info)

for owner, cats in owners.items():
    cats_str = "; ".join(cats)
    print(f"{owner}: {cats_str}")


print("\n")


"""
Задача 8: Редкое слово
Напишите программу, которая принимает на вход строку, и выводит слово, которое встречается во фразе реже всего.
Если редких слов несколько, нужно вывести то, которое меньше в лексикографическом порядке. Регистр слов не учитывается, знаки препинания в предложениях игнорируются.

дом, милый дом, милый. => дом
"""

s = "дом, милый дом, милый."
words = s.lower().replace(",", "").replace(".", "").split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

min_count = min(word_count.values())

# Фильтруем слова, которые встречаются реже всего, и выбираем минимальное
rare_words = [word for word in word_count if word_count[word] == min_count]
min_rare_word = min(rare_words)

print(min_rare_word)
print("\n")

"""
Напишите программу, которая принимает на вход две строки и определяет, являются ли они анаграммами.
Знаки препинания, пробелы и регистр при этом игнорируются.
"""

s1 = "Цари, вино и сало."
s2 = "Лисица и ворона."

# 1 вариант
set1 = sorted(s1.replace(",", "").replace(".", "").replace(" ", "").lower())
set2 = sorted(s2.replace(",", "").replace(".", "").replace(" ", "").lower())

print(("NO", "YES")[set1 == set2])

# 2 вариант
d = {}
for c in s1.lower():
    if c.isalpha():
        d[c] = d.get(c, 0) + 1
for c in s2.lower():
    if c.isalpha():
        d[c] = d.get(c, 0) - 1

print(("NO", "YES")[set(d.values()) == {0}])


print("\n")

"""
Задача 11: Расшифровка
На вход программе подается:
1. Зашифрованная строка.
2. N – число букв в словаре.
3. N строк, в которых в формате «буква: частота» указывается, сколько раз каждая буква встречается в слове.
Программа выводит расшифрованное слово.
Пример ввода:


Пример вывода:
banana

"""
crypt_str = "?*!*!*"
n = 3
str_data = ["b: 1", "a: 3", "n: 2"]

# Создаем словарь для хранения частоты букв
dic_str = {line.split(": ")[0]: int(line.split(": ")[1]) for line in str_data}

# Создаем обратный словарь для расшифровки (частота: буква)
freq_to_letter = {v: k for k, v in dic_str.items()}

# Создаем словарь для хранения частоты символов в зашифрованной строке
dic_crypt = {}
for symbol in crypt_str:
    if symbol in dic_crypt:
        dic_crypt[symbol] += 1
    else:
        dic_crypt[symbol] = 1

# Расшифровываем строку
decrypted_str = ""
for symbol in crypt_str:
    symbol_freq = dic_crypt[symbol]
    if symbol_freq in freq_to_letter:
        decrypted_str += freq_to_letter[symbol_freq]

print(decrypted_str)

print("\n")


"""
На вход программе подается количество пар синонимов n. Далее следует n строк, каждая строка содержит два слова-синонима.
После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.
"""
n = 4
in_str = [
    "Awful Terrible",
    "Beautiful Pretty",
    "Great Excellent",
    "Generous Bountiful",
    "Pretty",
]
d = dict((in_str[i].split() for i in range(n)))  # Создаем словарь из списка
ad = {v: k for k, v in d.items()}  # Создаем обратный словарь

key = in_str[n]
print(
    d.get(key, ad.get(key))
)  # Выводим значение по ключу из исходного словаря, если его нет, то из обратного

print("\n")


"""
Программа получает на вход количество стран n. Далее идет n строк, каждая строка начинается с названия страны,
 затем идут названия городов этой страны. В следующей строке записано число m, далее идут
m запросов — названия каких-то m городов, из перечисленных выше.

Программа должна вывести название страны, в которой находится данный город
"""
n = 2
n_str = [
    "Германия Берлин Мюнхен Гамбург Дортмунд",
    "Нидерланды Амстердам Гаага Роттердам Алкмар",
]
m = 4
m_str = ["Амстердам", "Гамбург", "Гаага", "Алкмар"]

d = {}
lis = [n_str[i].split() for i in range(n)]
for i in range(n):
    d.update(dict.fromkeys(lis[i][1:], lis[i][0]))

for i in range(m):
    print(d[m_str[i]])

print("\n")

"""
n — количество номеров телефонов, информацию о которых Тимур сохранил в телефонной книге.
В следующих n строках заданы телефоны и имена их владельцев через пробел.
m — количество поисковых запросов от Тимура.
В следующих m строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем (независимо от регистра имени). Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» (без кавычек).
Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.
"""
n = 3
n_str = ["79184219577 Женя", "79194249271 Руслан", "79281234567 Женя"]
m = 3
m_str = ["Руслан", "женя", "Вася"]

d = dict(n_str[i].split() for i in range(n))  # Создаем словарь из списка
for s in m_str:
    count = 0
    for k, v in d.items():
        if v.lower() == s.lower():
            print(k, end=" ")
            count = 1
    if count == 0:
        print("абонент не найден")
    else:
        print()

print("\n")
