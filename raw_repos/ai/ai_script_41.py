public class SortIntArray{
    public static void main(String[] args) {
        int[] intArray = {2, 5, 3, 1, 9, 4};

        Arrays.sort(intArray); 

        System.out.println("Sorted elements are:");
        for(int i : intArray){
            System.out.println(i);
        }
    }
}