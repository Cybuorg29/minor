public class FahrenheitToCelsius { 
  
    // F to C conversion formula 
    public static double fahrenheitToCelsius(double fahrenheit) { 
        return ((fahrenheit - 32) * 5) / 9; 
    } 
  
    public static void main(String[] args) { 
        double fahrenheit = 100; 
        double celsius = fahrenheitToCelsius(fahrenheit); 
        System.out.printf("%.2f degree Fahrenheit is equal to %.2f degree Celsius",fahrenheit,celsius); 
    } 
}