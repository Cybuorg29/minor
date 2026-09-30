import java.util.Hashtable;

public class HashtableExample {
     public static void main(String args[]) {
         Hashtable<Integer, String> ht = new Hashtable<Integer, String>();
 
         ht.put(1, "Code");
         ht.put(2, "Learn");
         ht.put(3, "Project");
         ht.put(4, "University");
 
         System.out.println("Hashtable: " + ht); 
     }
}