class Fibonacci 
{ 
    static int fib(int n) 
    { 
        if (n <= 1) 
            return n; 
        return fib(n-1) + fib(n-2); 
    } 
  
    public static void main (String args[]) 
    { 
        int num = 10, sum = 0; 
        for (int i = 1; i <= num; i++) 
        { 
            sum += fib(i); 
        } 
        System.out.println(sum); 
    } 
}