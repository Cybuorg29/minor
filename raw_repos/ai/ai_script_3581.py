// C# program to count occurrences of a string in a given text
using System;

namespace CountOccurrencesInString
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.";
            string pattern = "et";

            int count = 0;

            //Find the length of pattern
            int p_length = pattern.Length;

            //Iterate through the length of string
            for (int i = 0; i < text.Length - p_length+1; i++)
            {
                //Check if the substring matches the pattern
                if (text.Substring(i, p_length) == pattern)
                    count++;
            }
            Console.WriteLine("The occurrences of pattern \""+pattern+"\" in the text is: "+count);
        }
    }
}