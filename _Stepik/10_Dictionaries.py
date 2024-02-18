# Sample Input 1:
# *!*!*?
# 3
# а: 3
# н: 2
# с: 1
# Sample Output 1:
# ананас


# crypt_str = input()
# # Создаем словарь для хранения частоты букв str_data
# str_data = {}
# for _ in range(int(input())):
#     s = input().split(": ")
#     str_data[s[0]] = int(s[1])

# # Создаем обратный словарь для расшифровки (частота: буква)
# freq_to_letter = {v: k for k, v in str_data.items()}

# # Создаем словарь для хранения частоты символов в зашифрованной строке
# dic_crypt = {}
# for symbol in crypt_str:
#     dic_crypt[symbol] = dic_crypt.get(symbol, 0) + 1

# # Расшифровываем строку
# decrypted_str = ""
# for symbol in crypt_str:
#     symbol_freq = dic_crypt[symbol]
#     if symbol_freq in freq_to_letter:
#         decrypted_str += freq_to_letter[symbol_freq]

# print(decrypted_str)


numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i] ** 2 for i in range(len(numbers))}
print(result)

colors = {
    "c1": "Red",
    "c2": "Grey",
    "c3": None,
    "c4": "Green",
    "c5": "Yellow",
    "c6": "Pink",
    "c7": "Orange",
    "c8": None,
    "c9": "White",
    "c10": "Black",
    "c11": "Violet",
    "c12": "Gold",
    "c13": None,
    "c14": "Amber",
    "c15": "Azure",
    "c16": "Beige",
    "c17": "Bronze",
    "c18": None,
    "c19": "Lilac",
    "c20": "Pearl",
    "c21": None,
    "c22": "Sand",
    "c23": None,
}
result = {k: v for k, v in colors.items() if v is not None}
print(result)

# получить словарь result, состоящий из всех элементов словаря favorite_numbers , значения которых являются двузначными числами.
favorite_numbers = {
    "timur": 17,
    "ruslan": 7,
    "larisa": 19,
    "roman": 123,
    "rebecca": 293,
    "ronald": 76,
    "dorothy": 62,
    "harold": 36,
    "matt": 314,
    "kim": 451,
    "rosaly": 18,
    "rustam": 89,
    "soltan": 111,
    "amir": 654,
    "dima": 390,
    "amiran": 777,
    "geor": 999,
    "sveta": 75,
    "rita": 909,
    "kirill": 404,
    "olga": 271,
    "anna": 55,
    "madlen": 876,
}
result = {k: v for k, v in favorite_numbers.items() if 9 < v < 100}
print(result)

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря months , в которых ключ и значение поменялись местами.
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

result = {v: k for k, v in months.items()}
print(result)

# В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь result , в котором числа будут ключами, а слова – значениями.
# Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str)
s = "1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice"
result = {int(k): v for k, v in [l.split(":") for l in s.split()]}
print(result)

# Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка numbers,
# а значением – отсортированный по возрастанию список всех его делителей начиная с
numbers = [
    34,
    10,
    4,
    6,
    10,
    23,
    90,
    100,
    21,
    35,
    95,
    1,
    36,
    38,
    19,
    1,
    6,
    87,
    1000,
    13456,
    360,
]
result = {k: sorted([i for i in range(1, k + 1) if k % i == 0]) for k in numbers}
print(result)

# Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
# Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
# Примечание 2. Для получения ASCII кода символа используйте функцию ord()
words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik", "beegeek"]
result = {k: [ord(i) for i in k] for k in words}
print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря letters , за исключением тех, ключи которых есть в списке remove_keys.
letters = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    26: "Z",
}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {k: v for k, v in letters.items() if k not in remove_keys}
print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря students,
# где указан рост больше 167 см, а масса меньше 75 кг.

students = {
    "Timur": (170, 75),
    "Ruslan": (180, 105),
    "Soltan": (192, 68),
    "Roman": (175, 70),
    "Madlen": (160, 50),
    "Stefani": (165, 70),
    "Tom": (190, 90),
    "Jerry": (180, 87),
    "Anna": (172, 67),
    "Scott": (168, 78),
    "John": (186, 79),
    "Alex": (195, 120),
    "Max": (200, 110),
    "Barak": (180, 89),
    "Donald": (170, 80),
    "Rustam": (186, 100),
    "Alice": (159, 59),
    "Rita": (170, 80),
    "Mary": (175, 69),
    "Jane": (190, 80),
}
result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
print(result)

# Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый элемент каждого кортежа, а значением – кортеж из оставшихся двух элементов.
tuples = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
    (16, 17, 18),
    (19, 20, 21),
    (22, 23, 24),
    (25, 26, 27),
    (28, 29, 30),
    (31, 32, 33),
    (34, 35, 36),
]
result = {i[0]: (i[1], i[2]) for i in tuples}
print(result)

# Дополните приведенный код, используя генератор,
# так чтобы получить список result, содержащий вложенные словари в соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].
student_ids = [
    "S001",
    "S002",
    "S003",
    "S004",
    "S005",
    "S006",
    "S007",
    "S008",
    "S009",
    "S010",
    "S011",
    "S012",
    "S013",
]
student_names = [
    "Camila Rodriguez",
    "Juan Cruz",
    "Dan Richards",
    "Sam Boyle",
    "Batista Cesare",
    "Francesco Totti",
    "Khalid Hussain",
    "Ethan Hawke",
    "David Bowman",
    "James Milner",
    "Michael Owen",
    "Gary Oldman",
    "Tom Hardy",
]
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [
    {key: {key1: value1}}
    for key, key1, value1 in zip(student_ids, student_names, student_grades)
]

print()
print(result)


# Дополните приведенный код, чтобы в списках значений элементов словаря my_dict  не было чисел, больших 20. При этом порядок оставшихся элементов меняться не должен.
# Примечание. Необходимо изменить словарь my_dict, выводить ничего не надо.
my_dict = {
    "C1": [10, 20, 30, 7, 6, 23, 90],
    "C2": [20, 30, 40, 1, 2, 3, 90, 12],
    "C3": [12, 34, 20, 21],
    "C4": [22, 54, 209, 21, 7],
    "C5": [2, 4, 29, 21, 19],
    "C6": [4, 6, 7, 10, 55],
    "C7": [4, 8, 12, 23, 42],
    "C8": [3, 14, 15, 26, 48],
    "C9": [2, 7, 18, 28, 18, 28],
}

my_dict = {k: [i for i in v if i <= 20] for k, v in my_dict.items()}
print(my_dict)


# Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену.
# Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке, в формате username@domain
emails = {
    "nosu.edu": ["timyr", "joseph", "svetlana.gaeva", "larisa.mamuk"],
    "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
    "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
    "yandex.ru": ["surface", "google"],
    "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
    "mail.ru": ["angel.down", "joanne", "the.fame.moster"],
}

# Генерация списка всех электронных адресов
out_list = [
    f"{username}@{domain}"
    for domain, usernames in emails.items()
    for username in usernames
]

# Сортировка списка адресов в алфавитном порядке
out_list = sorted(out_list)

# Вывод адресов, каждый на отдельной строке
for email in out_list:
    print(email)

# Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:
# "G": "C", "C": "G", "T": "A", "A": "U"
# Напишите программу, переводящую цепь ДНК в цепь РНК.
# ACTG => UGAC

dict_dna_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
dna = "ACTG"
rna = "".join([dict_dna_rna[i] for i in dna])
print(rna)

# Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с учетом регистра.
# Для первого вхождения слова программа выведет 1, для второго вхождения того же слова — 2 и т. д.
# Sample Input 1: прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
# Sample Output 1: 1 1 2 1 1 2 1 2 3 1

text = "прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон"

words_count = {}
for word in text.split():
    words_count[word] = words_count.get(word, 0) + 1
    print(words_count[word], end=" ")
print()

# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.
# В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.

# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
# должен выводить:
# age=28&name=timur
# game=2&sport=hockey&time=17


def build_query_string(params):
    return "&".join([f"{k}={v}" for k, v in sorted(params.items())])


print(build_query_string({"sport": "hockey", "game": 2, "time": 17}))


# Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей переданного списка.
# Пример работы функции:
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result) # {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# ----------------
# Для каждого ключа создаёт в результирующем словаре множество, если такового ещё нет (используя метод get() со значением по умолчанию
# в виде пустого множества), и затем объединяет это множество с множеством, содержащим текущее значение.
# Оператор | используется для объединения множеств, что и требуется для решения задачи.
def merge(dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            result[k] = result.get(k, set()) | {v}
    return result
