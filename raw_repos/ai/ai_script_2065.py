class PrimeNumber
{
    public static void Main()
    {
        Console.Write("Enter a number: ");
        int n = int.Parse(Console.ReadLine());
 
        for (int i = 2; i <= n; i++)
        {
            if (CheckPrime(i))
            {
                Console.Write(i + " ");
            }
        }
        Console.WriteLine();
    }
 
    public static bool CheckPrime(int numberToCheck)
    {
        int boundary = (int)Math.Floor(Math.Sqrt(numberToCheck));
 
        if (numberToCheck == 1) return false;
        if (numberToCheck == 2) return true;
 
        for (int i = 2; i <= boundary; ++i)
        {
            if (numberToCheck % i == 0) return false;
        }
 
        return true;
    }
}