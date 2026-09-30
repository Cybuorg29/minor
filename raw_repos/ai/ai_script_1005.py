class Program 
{ 
    static void Main(string[] args) 
    { 
        // create an object of type Hello 
        Hello helloObject = new Hello(); 
       
        // call the SayHello method of the helloObject 
        helloObject.SayHello(); 
    } 
} 

// Create a class named Hello 
public class Hello 
{ 
    public void SayHello() 
    { 
        Console.WriteLine("Hello, World!"); 
    } 
}