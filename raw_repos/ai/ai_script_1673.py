public class MaxElement 
{
    public static void main(String[] args) 
    {
        int[] arr1 = {2, 8, 7, 2, 8, 2, 6};

        int count = 1;
        int max_element=arr1[0];
        int temp_count;
        for (int i = 0; i < arr1.length; i++)
        {
            temp_count = 1;
            for (int j = i+1; j < arr1.length; j++)
            {
                if(arr1[i] == arr1[j]){
                    temp_count++;
                }
            }

            if(temp_count > count){
                count = temp_count;
                max_element=arr1[i];
            }
        }
        
        System.out.println("Max Element : "+max_element);
    }
}