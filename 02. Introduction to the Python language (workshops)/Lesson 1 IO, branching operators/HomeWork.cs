public class Program
{

  public static void Main(string[] args)
  {
	Console.Clear();
	TaskOne();
	TaskToo();
	TaskThree();
	TaskFour();
  }


  public static void TaskOne()
  {
	Console.WriteLine("Задача 2: Найдите сумму цифр трехзначного числа n. Результат сохраните в переменную res");
	int n = 123;
	int res = 0;
	Console.Write($"Для числа {n} сумма цифр = ");

	for (int i = 0; i < 3; i++)
	{
	  res += n % 10;
	  n /= 10;
	}
	Console.WriteLine(res);
  }


  public static void TaskToo()
  {
	Console.WriteLine("\nЗадача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.");
	Console.WriteLine("Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,");
	Console.WriteLine("а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?");
	Console.WriteLine("Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей");

	int n = 24;
	int x = n / 6;
	Console.WriteLine($"Из {n} журавликов Петя сделал {x}, Катя {x * 4}, а Сергей {x}");
  }


  public static void TaskThree()
  {
	Console.WriteLine("\nЗадача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.");
	Console.WriteLine("Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.");
	Console.WriteLine("Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.");

	int n = 385917;
	int res = 0;
	Console.Write($"Билет {n} ");

	for (int i = 0; i < 3; i++)
	{
	  res += n % 10; // сумма трех последних чисел
	  n /= 10;
	}

	for (int i = 0; i < 3; i++)
	{
	  res -= n % 10; // отнимаем сумму трех первых чисел
	  n /= 10;
	}

	if (res == 0)
	{
	  Console.WriteLine("счастливый");
	}
	else
	{
	  Console.WriteLine("не счастливый");
	}
  }


  public static void TaskFour()
  {
	Console.WriteLine("\nЗадача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,");
	Console.WriteLine("если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).");

	int a = 3;
	int b = 3;
	int c = 6;
	Console.Write($"От шоколадки {a}х{b} {c} долек => ");

	if ((c <= b * a) && (c % a == 0) || (c % b == 0))
	{
	  Console.WriteLine("yes");
	}
	else
	{
	  Console.WriteLine("no");
	}
  }
}
