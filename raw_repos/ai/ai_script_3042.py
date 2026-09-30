// Define a polygon class
public class Polygon {
  // An array of Points to represent the vertices of a polygon
  private Point[] vertices;
 
  // A constructor that takes an array of Points
  public Polygon(Point[] vertices) {
    this.vertices = vertices;
  }
 
  // A method that returns the area of the polygon
  public double getArea() {
    double area = 0;
    int j = this.vertices.length - 1;
    for (int i = 0; i < this.vertices.length; i++) {
		area += (this.vertices[j].getX() + this.vertices[i].getX()) 
				* (this.vertices[j].getY() - this.vertices[i].getY());
		j = i; 
    }   
    return Math.abs(area / 2); 
  }
}