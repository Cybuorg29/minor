public class TriangleAreaCalculator {

    // Returns the area of the given triangle, given three points
    static double area(int x1, int y1, int x2, int y2, int x3, int y3){
        double side1 = Math.pow(Math.abs(x1-x2),2) + Math.pow(Math.abs(y1-y2),2);
        double side2 = Math.pow(Math.abs(x2-x3),2) + Math.pow(Math.abs(y2-y3),2);
        double side3 = Math.pow(Math.abs(x3-x1),2) + Math.pow(Math.abs(y3-y1),2);
        double sperimeter = (side1 + side2 + side3) / 2;
        double area = Math.sqrt(sperimeter*(sperimeter-side1)*(sperimeter-side2)*(sperimeter-side3));
        return area;
    }
    
    public static void main(String[] args) {
        int x1 = 0;
        int y1 = 0;
        int x2 = 3;
        int y2 = 4;
        int x3 = 4;
        int y3 = 0;
        
        System.out.println("The area of the triangle is: " + area(x1, y1, x2, y2, x3, y3));
    }
}