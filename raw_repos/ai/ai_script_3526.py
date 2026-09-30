public class Fibonacci { 
    public static void main(String[] args) { 
        int n = 10; 
        int num1=0, num2=1;
        System.out.print("Fibonacci Series of "+n+" numbers:");
 
        for (int i = 1; i <= n; ++i) {
            System.out.print(num1+" ");
            int sumOfPrevTwo = num1 + num2;
            num1 = num2;
            num2 = sumOfPrevTwo;
        }
    } 
}

// Output: Fibonacci Series of 10 numbers: 0 1 1 2 3 5 8 13 21 34