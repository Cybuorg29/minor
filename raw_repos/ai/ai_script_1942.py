import java.util.Scanner;

public class Program {    
    public static void main(String[] args) {      
        Scanner scanner = new Scanner(System.in);
        int num1 = 0;
        int num2 = 0;
        int result = 0;
       
        System.out.print("Enter two numbers separated by a space: ");
        num1 = scanner.nextInt();
        num2 = scanner.nextInt();
       
        result = num1 + num2;
       
        System.out.println("The sum of " + num1 + " and "
         + num2 + " is " + result);
    }
}