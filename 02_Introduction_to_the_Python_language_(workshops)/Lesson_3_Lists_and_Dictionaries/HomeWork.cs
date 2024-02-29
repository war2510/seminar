using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{

    public static void Main(string[] args)
    {
        Console.Clear();
        TaskOne();
        TaskToo();
        TaskThree();
        TaskFour();
        TaskFive();
        TaskSix();

    }

    public static void TaskOne()
    {
        Console.WriteLine("Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1. Найдите количество и выведите его");

        int[] list_1 = { 1, 3, 2, 3, 3, 4, 5 };
        int k = 3;
        Console.WriteLine($"Массив: [{string.Join(", ", list_1)}], k = {k}");

        int count = 0;
        foreach (int i in list_1)
        {
            if (i == k)
            {
                count++;
            }
        }

        Console.WriteLine($"Число {k} встречается {count} раз(а) в массиве.");
    }


    public static void TaskToo()
    {
        Console.WriteLine("\nТребуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.");
        Console.WriteLine("Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.");

        int[] list_1 = { 6, 2, 4, 3, 5, 1, 7 };
        int k = 8;
        int res = list_1[0];
        int minDiff = Math.Abs(list_1[0] - k);

        foreach (int i in list_1)
        {
            int currentDiff = Math.Abs(i - k);
            if (currentDiff < minDiff)
            {
                minDiff = currentDiff;
                res = i;
            }
        }

        Console.WriteLine($"Ближайший элемент к {k} в массиве: {res}");
    }



    public static void TaskThree()
    {
        Console.WriteLine("\nНапишите программу, которая вычисляет стоимость введенного пользователем слова.");

        var letterScores = new Dictionary<char, int>();
        var scores = new Dictionary<int, string>()
        {
            [1] = "AEIOULNSTRАВЕИНОРСТ",
            [2] = "DGДКЛМПУ",
            [3] = "BCMPБГЁЬЯ",
            [4] = "FHVWYЙЫ",
            [5] = "KЖЗХЦЧ",
            [8] = "JXШЭЮ",
            [10] = "QZФЩЪ"
        };

        // Предварительная обработка словаря
        foreach (var score in scores)
        {
            foreach (char letter in score.Value)
            {
                letterScores[letter] = score.Key;
            }
        }

        Console.Write("Введите слово: ");
        string inputWord = Console.ReadLine().ToUpper();

        int totalCost = 0;

        foreach (char letter in inputWord)
        {
            if (letterScores.TryGetValue(letter, out int letterScore))
            {
                totalCost += letterScore;
            }
        }

        Console.WriteLine($"Стоимость слова {inputWord} = {totalCost}");
    }


    public static void TaskFour()
    {
        Console.WriteLine("\nЗадача №21. Напишите программу для печати всех уникальных значений в словаре.");

        // Использование HashSet<string> для uniqueValues обеспечивает автоматическую уникальность значений без необходимости явной проверки.
        HashSet<string> uniqueValues = new();

        Dictionary<string, List<string>> dict = new()
        {
            ["V"] = new List<string> { "S001", "S002" },
            ["VI"] = new List<string> { "S001", "S005" },
            ["VII"] = new List<string> { " S005 " },
            [" V "] = new List<string> { " S009 " },
            [" VIII "] = new List<string> { " S007 " }
        };

        Console.WriteLine("Исходный словарь:");
        foreach (var entry in dict)
        {
            Console.WriteLine($"('{entry.Key}', [{string.Join(", ", entry.Value)}]");
            foreach (var value in entry.Value)
            {
                uniqueValues.Add(value);
            }
        }

        var sortedUniqueValues = uniqueValues.OrderBy(v => v).ToList();
        Console.WriteLine($"Уникальные значения: '{string.Join("', '", sortedUniqueValues)}'");
    }


    public static void TaskFive()
    {
        Console.WriteLine("\nВводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.");
        Console.WriteLine("Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров");
        Console.WriteLine("(следующих в том же порядке, что и во входной строке) с соответствующими кодами.");

        // Console.WriteLine("Введите номера телефонов через пробел:");
        // string input = Console.ReadLine();
        string input = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890";

        string[] phones = input.Split(' '); // Разбиваем строку на отдельные номера

        Dictionary<string, List<string>> d = new Dictionary<string, List<string>>();

        foreach (string phone in phones)
        {
            // Извлекаем код страны как подстроку, начиная с первого символа до первого встречного символа номера (которые могут быть от '2' до '9'), включая его
            string code = phone.Substring(0, phone.IndexOfAny(new char[] { '2', '3', '4', '5', '6', '7', '8', '9' }, 1) + 1);

            // Проверяем, существует ли уже такой код в словаре
            if (!d.ContainsKey(code))
            {
                d[code] = new List<string>(); // Если нет, создаем новый список для этого кода
            }
            d[code].Add(phone); // Добавляем номер телефона в список для его кода
        }

        // Сортируем ключи словаря перед выводом
        var sortedKeys = d.Keys.OrderBy(k => k);

        // Выводим отсортированные результаты
        foreach (var key in sortedKeys)
        {
            Console.WriteLine($"('{key}', [{string.Join(", ", d[key])}])");
        }
    }


    public static void TaskSix()
    {
        Console.WriteLine("\nЗадача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность");
        Console.WriteLine("(сдвиг - циклический) на K элементов вправо, K – положительное число");
        Console.WriteLine("k = 3	Input: [1, 2, 3, 4, 5]	Output: [3, 4, 5, 1, 2]");

        int[] arr = { 1, 2, 3, 4, 5 };
        int k = 3;
        Console.WriteLine($"Начальная последовательность: [{string.Join(", ", arr)}]");


        k = k % arr.Count();

        Console.WriteLine($"Сдвиг последовательности:	 [{string.Join(", ", arr[(k - 1)..])}, {string.Join(", ", arr[..(k - 1)])}]");
    }



    // string[] peopleRange = people[..4];
    // k = k % len(arr)
    // arr_un = arr[k - 1 :] + arr[: k - 1]
    // print(arr_un)


    // # Второй вариант решения
    // def move(lst, steps):
    //	 if steps > 0:
    //		 for i in range(steps):
    //			 lst.insert(0, lst.pop())


    // move(arr, k)
    // print(arr)
    // print()

}


