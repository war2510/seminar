def f(x):
    return x


print(f(5))
# --------
i1 = lambda a: a
print(i1(5))
# --------
print((lambda a: a)(5))
# --------
lst = "1 2 3 4 5".split()
print(lst)
# --------
lst1 = list(map(int, lst))
print(lst1)
# --------
lst2 = list(map(lambda a: a * 2, lst1))
print(lst2)
# --------
lst3 = list(filter(lambda a: a % 2, lst1))
print(lst3)
# --------
lst_new = [(7, 8), (9, 4), (5, 6)]
lst4 = list(filter(lambda a: (a[0] + a[1] < 12), lst_new))
print(lst4)
# --------
# lst_6 = list(map(int, input()))
# print(lst_6)

"""
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз
и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values)) if values == transformed_values:
print(‘ok’) else:
print(‘fail’)
Вывод:
ok
"""
values = [1, 23, 42, "asdfg"]
transformed_values = list(map(lambda a: a, values))
if values == transformed_values:
    print("ok")
else:
    print("fail")


"""
Задача No49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
"""
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# Вариант 1
print(*max(orbits, key=lambda pair: pair[0] * pair[1] * (pair[0] != pair[1])))


# Вариант 2
def find_farthest_orbit(list_of_orbits):
    s_list = [(i, i[0] * i[1]) for i in list_of_orbits if i[0] != i[1]]
    return max(s_list, key=lambda a: a[1])[0]


print(*find_farthest_orbit(orbits))

# Вариант 3
# Отфильтровываем круговые орбиты
S_orbit = list(filter(lambda a: a[0] != a[1], orbits))

# Находим максимальную площадь орбиты
orb_max = max(list(map(lambda a: a[0] * a[1], S_orbit)))

# Находим орбиту с максимальной площадью
max_orbit = list(filter(lambda a: a[0] * a[1] == orb_max, S_orbit))

print(*max_orbit)


"""
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику.
"""
values = [0, 10, 6, 8]


def same_by(characteristic, objects):
    return min(map(characteristic, objects)) == max(map(characteristic, objects))


if same_by(lambda x: x % 2, values):
    print("sam")
else:
    print("different")
