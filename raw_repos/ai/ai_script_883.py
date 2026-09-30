public class ComplexNumber {
  private double x;
  private double y;
 
  public ComplexNumber(double x, double y) {
    this.x = x;
    this.y = y;
  }
  
  public double getMagnitude() {
    return Math.sqrt(x * x + y * y);
  }
  
  public void increment() {
    this.x++;
    this.y++;
  }
}