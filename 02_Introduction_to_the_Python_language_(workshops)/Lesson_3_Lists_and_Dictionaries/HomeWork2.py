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
list1 = list()

for k, v in emails.items():
    for i in v:
        list1.append(f"{i}@{k}")
list1.sort()
print(*list1, sep="\n")
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

dict_rights_f = {}
for i in rights_f:
    for j in range(1, len(i.split())):
        if i.split()[0] in dict_rights_f:
            dict_rights_f[i.split()[0]].append(i.split()[j])
        else:
            dict_rights_f[i.split()[0]] = [i.split()[j]]

for i in q_access:
    r = rights[i.split()[0]]
    if i.split()[1] in dict_rights_f and r in dict_rights_f[i.split()[1]]:
        print("OK")
    else:
        print("Access denied")

print("\n")


"""
Задача 5: Продажи
Напишите программу, которая подсчитывает количество единиц товаров, приобретенных покупателями онлайн-магазина.
"""
s = [
    "Сергей Карандаш 3",
    "Андрей Тетрадь 5",
    "Юлия Линейка 1",
    "Сергей Ручка 2",
    "Юлия Книга 4",
]

word_count = {}

for sell in s:
    a, b, c = sell.split()
    if a in word_count:
        word_count[a].append(f"{b} {c}")
    else:
        word_count[a] = [f"{b} {c}"]


for k, v in word_count.items():
    print(f"{k}:")
    for i in v:
        print(i)

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

word_count = {}
for cat in cats:
    a, b, c, d = cat
    if f"{c} {d}" in word_count:
        word_count[f"{c} {d}"].append(f"{a}, {b}")
    else:
        word_count[f"{c} {d}"] = [f"{a}, {b}"]

for k, v in word_count.items():
    print(f"{k}:", end=" ")
    for i in v:
        print(i, end="; ")
    print()

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

s1 = sorted(s1.replace(",", "").replace(".", "").replace(" ", "").lower())
s2 = sorted(s2.replace(",", "").replace(".", "").replace(" ", "").lower())

if s1 == s2:
    print("YES")
else:
    print("NO")


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
dic_str = ["b: 1", "a: 3", "n: 2"]

dic_str = dict(dic_str)
print(dic_str)

"""
Задача 12: Запрос
Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса, сформированную из отсортированных в лексикографическом порядке параметров.
Пример:
Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:
challenge=17&course=python&lesson=2
    
"""
