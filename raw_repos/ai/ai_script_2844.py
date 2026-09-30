import java.util.Scanner;

public class ReverseString 
{
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = in.nextLine();
        in.close();

        char[] arr = str.toCharArray();

        for (int i = arr.length - 1; i >= 0; i--) 
        {
            System.out.print(arr[i]);
        }
    }
}