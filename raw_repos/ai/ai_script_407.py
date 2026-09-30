public class Fibonacci{
	public static int findFibonacci(int n){
		if(n == 0){
			return 0;
		}
		if(n == 1){
			return 1;
		}
		return findFibonacci(n-1) + findFibonacci(n-2);
	}
	
	public static void main(String args[]){
		Scanner in = new Scanner(System.in);
		System.out.println("Enter a number:");
		int n = in.nextInt();
		System.out.println("The Fibonacci number is " +
							findFibonacci(n));
	}
}