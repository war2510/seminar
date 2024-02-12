public class Program
{
  public static void Main(string[] args)
  {
	Console.Clear();
	TaskOne();
	TaskToo();
	TaskThree();
  }

  public static void TaskOne()
  {
	Console.WriteLine("На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток,");
	Console.WriteLine("которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.");
	Console.WriteLine("На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх.");
	Console.WriteLine("Размер списка не превышает 1000 элементов. Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.");

	int[] coins = new int[] { 0, 1, 0, 1, 1, 0, 1, 0, 0 };

	int count1 = 0; // Количество монет решкой вверх
	int count2 = 0; // Количество монет гербом вверх

	foreach (int coin in coins)
	{
	  if (coin == 0)
		count1++;
	  else
		count2++;
	}

	// Определяем, какая сторона окажется вверх после переворота минимального количества монет
	string sideUp = count1 < count2 ? "гербом" : "решкой";
	int minFlips = Math.Min(count1, count2);

	Console.WriteLine($"Минимальное число монеток, которые нужно перевернуть: {minFlips}. В итоге все монетки будут лежать {sideUp} в массиве [{string.Join(", ", coins)}].");
  }


  public static void TaskToo()
  {
	Console.WriteLine("\nПетя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.");
	Console.WriteLine("Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.");
	Console.WriteLine("Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.");
	Console.WriteLine("В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.");
	// y = s - x
	// x * (s - x) == p

	int s = 12;
	int p = 27;

	for (int x = 0; x <= 1000; x++)
	{
	  if (x * (s - x) == p && x <= s - x)
	  {
		Console.WriteLine($"{x} {s - x}");
	  }
	}

  }


  public static void TaskThree()
  {
	Console.WriteLine("\nТребуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.");

	int n = 160;
	int res = 1;

	while (res <= n)
	{
	  Console.Write($"{res} ");
	  res *= 2;
	}
	Console.WriteLine("\n");
  }
}
