public class Rectangle { 
    int length, width; 
  
    // Constructor 
    public Rectangle(int length, int width) 
    { 
        this.length = length; 
        this.width = width; 
    }

    public int getPerimeter() 
    { 
        // Calculate perimeter 
        return 2*(length + width); 
    } 
  
    public int getArea() 
    { 
        // Calculate area 
        return length*width; 
    } 
}