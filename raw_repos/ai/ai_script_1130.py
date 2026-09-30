using System;

namespace StringLength
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please enter a string: ");
            string input = Console.ReadLine();
            Console.WriteLine($"The length of the string is: {input.Length}");
        }
    }
}