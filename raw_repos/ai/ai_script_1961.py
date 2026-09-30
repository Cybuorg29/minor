public class PrimeFinder {
 
    public static void main(String[] args) { 
        int count = 0;
        int num = 1;
 
        while(count < 5) {
            num = num + 1;
            if (isPrime(num)) {
                System.out.println(num);
                count++;
            }
        }
    }
 
    public static boolean isPrime(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}