public class SortDescending { 
    public static void main(String[] args) 
    {
        int[] numbers = {3,8,5,1,2,6,4};
        int temp = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                if (numbers[i] < numbers[j]) {
                    //swap elements
                    temp = numbers[i]; // assign value of i to temp
                    numbers[i] = numbers[j];  // assign value of j to i
                    numbers[j] = temp;  // assign value of temp to j
                }
            }
        }
        System.out.println("Array elements in descending order:");
        for (int i = 0; i < numbers.length; i++) { 
            System.out.print(numbers[i]+" "); 
        } 
    }
}