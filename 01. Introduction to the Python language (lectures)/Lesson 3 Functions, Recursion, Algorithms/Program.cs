internal class Program
{
  private static void Main()
  {
	Console.Clear();

	Fib(); // Fibonacci
	InitQuickSort(); // Быстрая сортировка
	InitMergeSort(); // Сортировка слиянием
  }


  static void Fib() // Fibonacci
  {
	int[] list1 = new int[10];
	for (int i = 1; i <= 10; i++)
	{
	  list1[i - 1] = Fibonacci(i);
	}
	Console.WriteLine($"Fibonacci: [{string.Join(", ", list1)}]\n");

	static int Fibonacci(int n)
	{
	  if (n <= 1)
	  {
		return n;
	  }
	  return Fibonacci(n - 1) + Fibonacci(n - 2);
	}

  }


  static void InitQuickSort()
  {
	int[] list1 = new int[] { 5, 3, 8, 4, 2, 7, 1, 10, 6, 9 };

	Console.WriteLine($"Original:  [{string.Join(", ", list1)}]");
	QuickSort(list1, 0, list1.Length - 1);
	Console.WriteLine($"QuickSort: [{string.Join(", ", list1)}]\n");
  }

  static void QuickSort(int[] arr, int start, int end) // Быстрая сортировка
  {
	if (start < end)
	{
	  int pivotIndex = Partition(arr, start, end);
	  QuickSort(arr, start, pivotIndex - 1); // Сортировка левой части
	  QuickSort(arr, pivotIndex + 1, end); // Сортировка правой части
	}
  }

  static int Partition(int[] arr, int start, int end)
  {
	int pivot = arr[end];
	int i = start - 1;
	for (int j = start; j < end; j++)
	{
	  if (arr[j] < pivot)
	  {
		i++;
		Swap(ref arr[i], ref arr[j]);
	  }
	}
	Swap(ref arr[i + 1], ref arr[end]);
	return i + 1;
  }

  static void Swap(ref int a, ref int b)
  {
	int temp = a;
	a = b;
	b = temp;
  }

  static void InitMergeSort() // Сортировка слиянием
  {
	int[] list1 = new int[] { 5, 3, 8, 4, 2, 7, 1, 10, 6, 9 };

	Console.WriteLine($"Original:  [{string.Join(", ", list1)}]");
	MergeSort(list1, 0, list1.Length - 1);
	Console.WriteLine($"MergeSort: [{string.Join(", ", list1)}]\n");
  }

  static int[] MergeSort(int[] arr, int start, int end) // Сортировка слиянием
  {
	if (start < end)
	{
	  int middle = (start + end) / 2;
	  MergeSort(arr, start, middle);
	  MergeSort(arr, middle + 1, end);
	  Merge(arr, start, middle, end);
	}
	return arr;
  }

  static void Merge(int[] arr, int start, int middle, int end) // Слияние
  {
	int leftLength = middle - start + 1;
	int rightLength = end - middle;

	int[] left = new int[leftLength];
	int[] right = new int[rightLength];

	for (int i = 0; i < leftLength; i++)
	{
	  left[i] = arr[start + i];
	}
	for (int i = 0; i < rightLength; i++)
	{
	  right[i] = arr[middle + 1 + i];
	}

	int leftIndex = 0;
	int rightIndex = 0;
	int mergedIndex = start;

	while (leftIndex < leftLength && rightIndex < rightLength)
	{
	  if (left[leftIndex] <= right[rightIndex])
	  {
		arr[mergedIndex] = left[leftIndex];
		leftIndex++;
	  }
	  else
	  {
		arr[mergedIndex] = right[rightIndex];
		rightIndex++;
	  }
	  mergedIndex++;
	}

	while (leftIndex < leftLength)
	{
	  arr[mergedIndex] = left[leftIndex];
	  leftIndex++;
	  mergedIndex++;
	}

	while (rightIndex < rightLength)
	{
	  arr[mergedIndex] = right[rightIndex];
	  rightIndex++;
	  mergedIndex++;
	}
  }
}
