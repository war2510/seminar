internal class Program
{
	private static void Main(string[] args)
	{
		Console.Clear();
		TaskOne();
		TaskToo();
		TaskThree();
		TaskFour();
		//TaskFive();
		//TaskSix();
	}


	public static void TaskOne() // Задача 1
	{
		Console.WriteLine("\nДаны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.");

		string var2 = "1 3 5 7 9";  // элементы первого множества через пробел
		string var3 = "2 3 4 5";  // элементы второго множества через пробел
		Console.WriteLine("Первое множество: " + var2);
		Console.WriteLine("Второе множество: " + var3);

		// Преобразование строк в массивы целых чисел. Используем множества (HashSet<int>) для удаления повторений
		var set1 = var2.Split(' ').Select(int.Parse).ToHashSet();
		var set2 = var3.Split(' ').Select(int.Parse).ToHashSet();

		// Находим пересечение множеств, чтобы получить общие элементы
		var commonElements = set1.Intersect(set2);

		// Сортируем результат и выводим
		var sortedCommonElements = commonElements.OrderBy(x => x).ToArray();
		Console.WriteLine("Пересечение множеств: " + string.Join(" ", sortedCommonElements) + "\n");
	}


	public static void TaskToo() // Задача 2
	{
		Console.WriteLine("\nНа вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.");
		Console.WriteLine("Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль с трех соседних кустов.");
		int[] arr = { 5, 8, 6, 4, 9, 2, 7, 3 };
		Console.WriteLine($"Урожайность кустов: {string.Join(" ", arr)}");

		int res;
		if (arr.Length < 3)
		{
			Console.WriteLine("Количество кустов меньше трех");
		}
		else
		{
			res = arr[0] + arr[1] + arr[2];
			for (int i = 0; i < arr.Length; i++)
			{
				int sum_current = arr[i] + arr[(i + 1) % arr.Length] + arr[(i + 2) % arr.Length];
				res = Math.Max(res, sum_current);
			}
			Console.WriteLine("Максимальное количество ягод: " + res + "\n");
		}
	}


	public static void TaskThree() // Задача 3
	{
		Console.WriteLine("\nНапишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.");
		string input_str = "a a a b c a a d c d d";
		Console.WriteLine("Input: " + input_str);
		Console.Write("Output: ");

		string[] characters = input_str.Split(' ');
		Dictionary<string, int> char_count = new();

		foreach (var item in characters)
		{
			if (char_count.ContainsKey(item))
			{
				Console.Write($" {item}_{char_count[item]}");
				char_count[item] += 1;
			}
			else
			{
				Console.Write($" {item}");
				char_count[item] = 1;
			}
		}
		Console.WriteLine("\n");
	}


	public static void TaskFour() // Задача 4
	{
		Console.WriteLine("\nПользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.");

		string input_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells";
		Console.WriteLine("Input: " + input_str);

		var words = input_str.Trim().Replace(".", " ").ToLower().Split(' ').ToHashSet();

		Console.WriteLine("Output: " + string.Join(" ", words));
		Console.WriteLine($"Число слов: {words.Count}\n");
	}
}
