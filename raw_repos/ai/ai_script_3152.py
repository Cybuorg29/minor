public class NumberAdder {

    int sum = 0; 
  
    // Method to add the given numbers
    public void addNumbers(int[] numbers) {
        for (int i = 0; i < numbers.Length; i++){
            this.sum += numbers[i]; 
        }
    }

}