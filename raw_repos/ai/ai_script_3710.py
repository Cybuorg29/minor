import java.util.ArrayList;
import java.util.Collections;

public class SortListAscending {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(10);
        list.add(1);
        list.add(8);

        Collections.sort(list);

        System.out.println("The list in ascending order is: " + list);
    }
}