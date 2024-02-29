print("\033[H\033[J")  # Очистка консоли

"""
В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)
"""

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []

# Вариант 1
for numbers in data:
    if not numbers % 2:
        out.append((numbers, numbers * numbers))

print(out)


# Вариант 2
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


res = select(int, data)  # Или map(int, data)
print(res)  # [1, 2, 3, 5, 8, 15, 23, 38]

res = where(lambda x: x % 2 == 0, res)  # Или filter(lambda x: x % 2 == 0, res)
print(res)  # [2, 8, 38]

res = list(select(lambda x: (x, x**2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]
print("\n")


"""
Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как
превратить list строк в list чисел?
"""
data = "1 2 3 5 8 15 23 38"

data = list(map(int, data.split()))
print(data)  # [1, 2, 3, 5, 8, 15, 23, 38]
print("\n")


print("# Функция zip () пробегает по минимальному входящему набору:")
users = ["user1", "user2", "user3", "user4", "user5"]
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
print(
    users, ids, salary
)  # ['user1', 'user2', 'user3', 'user4', 'user5'] [4, 5, 9, 14, 7] [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
print("\n")


print("# Функция enumerate() позволяет пронумеровать набор данных.")
users = ["user1", "user2", "user3"]
print(users)  # ['user1', 'user2', 'user3']

data = list(enumerate(users))
print(data)  # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
