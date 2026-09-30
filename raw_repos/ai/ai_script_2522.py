import org.springframework.boot.autoconfigure.SpringBootApplication; 

@SpringBootApplication 
public class App 
{ 
    // Function to calculate the area of triangle 
    public static double calculateArea(int a, int b, int c) 
    { 
        double s = (a + b + c) / 2; 
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c)); 
        return area; 
    } 
  
    public static void main( String[] args ) 
    { 
        int a = 3; 
        int b = 4; 
        int c = 5; 
        System.out.println("The area of the triangle is: " + calculateArea(a, b, c)); 
    } 
}