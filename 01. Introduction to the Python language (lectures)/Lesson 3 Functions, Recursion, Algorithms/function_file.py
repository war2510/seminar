def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    return  # выход из функции


# Можно указать значение переменной count по умолчанию. Например, если значение явно не указано (нет второго аргумента), по умолчанию значение переменной count равно трем.
def new_string(symbol, count=3):
    return symbol * count
