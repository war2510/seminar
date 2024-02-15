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
print("\n\n")


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

dict = {}

for sell in s:
	a, b, c = sell.split()
	if a in dict:
		dict[a].append(f"{b} {c}")
	else:
		dict[a] = [f"{b} {c}"]


for k, v in dict.items():
	print(f"{k}:")
	for i in v:
		print(i)

print("\n\n")
