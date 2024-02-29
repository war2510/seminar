print("\033[H\033[J")  # Очистка консоли

# Задание 1
"""
Дан файл california_housing_train.csv. Определить среднюю стоимость дома,
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""
import pandas as pd

df = pd.read_csv("california_housing_train.csv.zip")

avg = df[(df["population"] > 0) & (df["population"] < 500)][
    "median_house_value"
].mean()  # Средняя стоимость дома, где количество людей от 0 до 500

print(avg)

# Задание 2
"""
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population
и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
"""
min_population = df["population"].min()
print(min_population)

max_households_in_min_population = df.loc[df["population"] == min_population][
    "households"
].max()

print(max_households_in_min_population)
