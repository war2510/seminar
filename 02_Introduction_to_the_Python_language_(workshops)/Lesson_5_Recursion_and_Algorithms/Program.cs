
internal class Program
{
	private static void Main()
	{
		Console.Clear();

		Example01(); // Найти n-ое число Фибоначчи через рекурсию
		Example02();
		Example03();
		Example04();

	}

	static void Example01()
	{
		Console.WriteLine("Найти n-ое число Фибоначчи через рекурсию");

		Console.Write("Введите число: ");
		int n = int.Parse(Console.ReadLine());
		Console.WriteLine($"Число Фибоначчи: {Fib(n)}\n");

		int Fib(int n)
		{
			if (n == 0) return 0;
			if (n == 1) return 1;
			return Fib(n - 1) + Fib(n - 2);
		}
	}

	static void Example02()
	{
		Console.WriteLine("Найти факториал n через рекурсию");

		Console.Write("Введите число: ");
		int n = int.Parse(Console.ReadLine());
		Console.WriteLine($"Факториал: {Factorial(n)}\n");

		int Factorial(int n)
		{
			if (n == 0) return 1;
			return n * Factorial(n - 1);
		}

	}
	static void Example03()
	{
		Console.WriteLine("Напишите функцию, которая с помощью рекурсии определяет, является ли введенное число простым или составным.");
		Console.Write("Введите число: ");
		int n = int.Parse(Console.ReadLine());
		Console.WriteLine($"Это число является простым: {Simple(n)}\n");

		bool Simple(int n, int i = 2)
		{
			if (n < 2) return false;
			if (i * i > n) return true;
			if (n % i == 0) return false;
			return Simple(n, i + 1);
		}
	}

	static void Example04()
	{
		Console.WriteLine("Дано натуральное число n и последовательность из n элементов. Надо вывести эту последовательность в обратном порядке");
		Console.Write("Введите число: ");
		int n = int.Parse(Console.ReadLine());
		int[] arr = new int[n];
		for (int i = 0; i < n; i++)
		{
			arr[i] = new Random().Next(1, 100);
			Console.Write($"{arr[i]} ");
		}

		Console.Write("==> ");
		string result = Reverse(arr, n);
		Console.WriteLine(result);

		Reverse(arr, n);  // Вызов функции вывода массива в обратном порядке;

		static string Reverse(int[] arr, int n)
		{
			if (n == 0) return "";
			return $"{arr[n - 1]} " + Reverse(arr, n - 1);
		}
		Console.WriteLine();
	}
}
