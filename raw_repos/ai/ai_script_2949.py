public class PrimeNumbers {
   public static void main(String[] args) {
      int N = 25;
      for (int i = 2; i < N; i++) { 
          int count = 0; 
          for (int j = 2; j <= Math.sqrt(i); j++) {
              if (i % j == 0) {
                  count++; 
                  break; 
              }
          }
          if (count == 0) {
              System.out.print(i + " "); 
          }
      }         
   }
}