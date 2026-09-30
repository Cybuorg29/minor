class Circle {
	private double radius;

	public Circle(double radius) {
		this.radius = radius;
	}

	public double getCircumference() {	
		return 2 * Math.PI * this.radius;
	}

	public double getArea() {
		return Math.PI * this.radius * this.radius;	
	}
}

class Rectangle {
	private double width;
	private double length;

	public Rectangle(double width, double length) {
		this.width = width;
		this.length = length;
	}

	public double getCircumference() {
		return 2*(this.width + this.length);
	}

	public double getArea() {
		return this.width * this.length;
	}
}