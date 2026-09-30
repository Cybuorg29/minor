// Code to create an ArrayList in Java
import java.util.ArrayList;

public class Demo {
    public static void main(String[] args) {
        // create an arraylist
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("C++");
        list.add("Python");
        System.out.println(list);

        // print the size of the list
        System.out.println("The size of the list is: "+list.size());
    }
}