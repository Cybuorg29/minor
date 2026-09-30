// Base class 
class Vehicle 
{ 
   String brand = "Ford"; 
   public void honk() 
   { 
      System.out.println("Tuut, tuut!"); 
   } 
} 
  
// sub class 
class Car extends Vehicle 
{ 
   String modelName = "Mustang"; 
   public static void main(String[] args) 
   { 
      // Create an object of Car 
      Car myCar = new Car(); 
  
      // Call the honk method (From the Vehicle class) on the myCar object 
      myCar.honk(); 
  
      // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class 
      System.out.println(myCar.brand + " " + myCar.modelName);   
   } 
}