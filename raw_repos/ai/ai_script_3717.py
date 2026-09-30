public class AverageCalculation 
{
    public static void main(String[] args) 
    {
        int[] inputArray = {2, 5, 7, 8, 9, 10};
        double sum = 0.0;
        // calculate the sum of elements
        for(int i = 0; i < inputArray.length; i++) {
            sum += inputArray[i];
        }
        // calculate the average
        double average = sum / inputArray.length;
        System.out.println("Average of Array Elements is: " + average); 
    }
}