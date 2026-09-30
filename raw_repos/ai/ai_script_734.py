public class PrimeNumber
{
 static void Main()
 {
 int n1 = 2;
 int n2 = 10;
 while (n1 < n2)
 {
 bool isPrime = true;
 for (int i = 2; i <= n1 / 2; i++)
 {
 if (n1 % i == 0)
 {
 isPrime = false;
 break;
 }
 }
 if (isPrime)
 Console.Write(n1 + " ");
 n1++;
 }
 }
}