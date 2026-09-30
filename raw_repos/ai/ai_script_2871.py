public class Fibonacci { 
  
    // Function to print the nth 
    // fibonacci number 
    static void printFibonacciSeries(int n) 
    { 
        int a = 0, b = 1, c; 
        if (n == 0) {
            System.out.print(a); 
            return; 
        }
        for (int i = 2; i <= n; i++) { 
            c = a + b; 
            System.out.print(c + " "); 
            a = b; 
            b = c; 
        } 
    } 
  
    // Driver Code 
    public static void main(String[] args) 
    { 
        int n = 10; 
        printFibonacciSeries(n); 
    } 
}