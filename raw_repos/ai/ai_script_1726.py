"""
Using Java, create a program to compute the area of a circle given the radius.
"""
 
public class AreaCircle {
   public static void main(String[] args) {
      double radius = 7.5;
      double area;
   
      area = Math.PI * Math.pow(radius, 2);
      System.out.println("Area of the circle is: " + area);
   }
}