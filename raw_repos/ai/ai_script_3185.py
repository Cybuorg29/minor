import java.util.HashMap; 

public class FruitMap 
{ 
    public static void main(String args[]) 
    { 
  
        // Creating a HashMap of fruit name 
        // and their corresponding prices 
        HashMap<String, Double> fruitMap = new HashMap<>(); 
  
        // Mapping string values to double 
        fruitMap.put("Mango", 2.4); 
        fruitMap.put("Orange", 1.4); 
        fruitMap.put("Apple", 3.2); 
  
        // Displaying the HashMap 
        System.out.println(fruitMap); 
    } 
}