# Метод pop удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())  # 0
print(list_1)  # [12, 7, -1, 21]
print(list_1.pop())  # 21
print(list_1)  # [12, 7, -1]
print(list_1.pop())  # -1
print(list_1)  # [12, 7]

# Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0))  # 12
print(list_1)  # [7, -1, 21, 0]

# Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1)  # [12, 7, 11, -1, 21, 0]

# Словари
dictionary = {}
dictionary = {"up": "↑", "left": "←", "down": "↓", "right": "→"}
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary["left"])  # ←
# типы ключей могут отличаться
print(dictionary["up"])  # ↑
# типы ключей могут отличаться
dictionary["left"] = "⇐"
print(dictionary["left"])  # ⇐
print(dictionary["type"])  # KeyError: 'type'
del dictionary["left"]  # удаление элемента
for item in dictionary:  # for (k,v) in dictionary.items():
    print("{}: {}".format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# Множества
colors = {"red", "green", "blue"}
print(colors)  # {'red', 'green', 'blue'}
colors.add("red")
print(colors)  # {'red', 'green', 'blue'}
colors.add("gray")
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove("red")
print(colors)  # {'green', 'blue','gray'}
colors.remove("red")  # KeyError: 'red'
colors.discard("red")  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

# Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})

# List Comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.
# list_1 = [exp for item in iterable (if conditional)]
list_1 = [i for i in range(1, 101) if i % 2 == 0]  # [2, 4, 6,..., 100]
list_1 = [
    (i, i) for i in range(1, 101) if i % 2 == 0
]  # [(2, 2), (4, 4),..., (100, 100)]

# Словари
squares = {i: i**2 for i in range(6)}
squares = {i: i**2 for i in range(10) if i % 2 == 0}

# Мы можем использовать вложенные циклы для создания словарей:
squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}

# Общий вид генератора словаря следующий:
# {ключ: значение for переменная in последовательность}
# где переменная — имя некоторой переменной,
# последовательность — последовательность значений, которые она принимает (любой итерируемый объект),
# ключ: значение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной,
# которой будут заполнены элементы словаря.
