"""
Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
При решении задачи используйте комбинацию функций filter, map, sum.
Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
"""

list1 = [a for a in range(10, 100)]
list2 = list(map(lambda b: b * b, list(filter(lambda a: a % 9 == 0, list1))))

print(list2)
print(sum(list2))

# print(sum(map(lambda x: x * x, filter(lambda x: x % 9 == 0, range(10, 100)))))
