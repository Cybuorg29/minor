public class Fibonacci { 
  
    public static void FibonacciN(int n) { 
        int i, f=0, s=1; 
  
        if (n == 1) 
            System.out.print(f+ " "); 
  
        else { 
            System.out.print(f+" "+s+" "); 
  
            for (i = 2; i < n; i++) { 
                int next = f + s; 
                System.out.print(next+" "); 
                f= s; 
                s = next; 
            } 
        } 
    } 
}