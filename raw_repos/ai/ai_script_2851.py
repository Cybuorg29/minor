public class Fibonacci {

    public static void printFibonacci(int n) {
        int n1 = 0, n2 = 1;
        for (int i = 0; i < n; i++) {
            System.out.print(n1 + " ");
            int sum = n1 + n2;
            n1 = n2;
            n2 = sum;
        }
    }
}