print("\033[H\033[J")  # Очистка консоли


# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


n = int(input("Введите число: "))  # 5
print(sumNumbers(n))  # 15
print("\n")


# Возможность передачи неограниченного количества аргументов
# - Можно указать любое количество значений аргумента функции.
# - Перед аргументом надо поставить *.
def sum_str(*params):
    res = ""
    for item in params:
        res += str(item)
    return res


print(sum_str("a", "s", "d", "w"))  # asdw
print(sum_str("a", "1"))  # a1
print(sum_str(1, 2, 3, 4))  # TypeError: ...
print("\n")


# function_file.py (Новый Python файл, в котором находятся функция f(x))
import function_file

print(function_file.f(1))
print("\n")

print(function_file.new_string("!", 5))  # !!!!!
print(function_file.new_string("!"))  # !!!
print(function_file.new_string(4))  # 12
print("\n")


# Рекурсия — это функция, вызывающая сама себя.
# Внутри функции fib(n), мы сначала задаем базис, если число n равно 1 или 2, это означает, что первое число и второе число последовательности равны 1.
# Мы так и делаем возвращаем 1. Как мы ранее проговорили: “Последовательно Фибоначчи, это такая последовательность, в которой каждое последующее число
# равно сумме 2-ух предыдущих”. Так и делаем, складываем на 2 предыдущих числа друг с другом и получаем 3.
def Fib(n):
    if n in [1, 2]:
        return 1
    return Fib(n - 1) + Fib(n - 2)


list_1 = []
for i in range(1, 10):
    list_1.append(Fib(i))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]
print("\n")


# Quick sort (Быстрая сортировка)
def QuickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(greater)


print(QuickSort([10, 5, 2, 3, 8]))


# merge sorting (сортировка слиянием)
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
MergeSort(list1)
print(list1)  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
