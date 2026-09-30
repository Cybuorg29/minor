public class FindFirstIndex {
    public static void main(String[] args) {
        int[] array = {1, 7, 3, 6, 4, 7};
        int num = 7;

        int idx = -1;
        for(int i = 0; i < array.length; i++) {
            if(array[i] == num) {
                idx = i;
                break;
            }
        }
        System.out.println("Index of the first occurrence of the given element: " + idx);
    }
}