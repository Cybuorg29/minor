import java.util.Random; 

public class RandomArray {
    public static void main(String[] args) {
        Random rand = new Random(); 
  
        float array[] = new float[10];  
  
        for(int i = 0; i < 10; i++) { 
            array[i] = rand.nextFloat(); 
        }
  
        System.out.println("Array of 10 random numbers between 0 and 1: ");
        for (int i = 0; i < 10; i++) { 
            System.out.println(array[i]); 
        } 
    }
}