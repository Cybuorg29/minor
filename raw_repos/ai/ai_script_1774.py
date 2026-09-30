public class Fibonacci {

  public static int getFibonacciNumber(int index) {
    // base cases
    if (index == 0) {
      return 0;
    }
    if (index == 1 || index == 2) {
      return 1;
    }
    // recursive case
    return getFibonacciNumber(index - 1) + getFibonacciNumber(index - 2);
  }
}