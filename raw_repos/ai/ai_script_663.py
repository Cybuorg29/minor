public class TriangleArea {
 
 public static void main(String[] args) {
 
  int a = 3;
  int b = 4;
  int c = 5;
 
  // calculate the semi-perimeter
  double s = (a + b + c) / 2;
 
  // calculate the area
  double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
 
  // display the result
  System.out.println("The area of the triangle: " + area);
 }
 
}