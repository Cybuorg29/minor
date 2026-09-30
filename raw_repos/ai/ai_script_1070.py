public class AreaCalculator {
    public static final double PI = 3.14159;
    
	public static double calculateArea(double radius) {
		return PI * radius * radius;
	}
    
	public static void main(String[] args) {
		System.out.println(calculateArea(10));
	}
}