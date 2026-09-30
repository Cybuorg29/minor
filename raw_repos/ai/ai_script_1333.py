public class MaximumPairSum { 

    static int findMaximumPairSum(int arr[]) { 
        int max1 = Integer.MIN_VALUE; 
        int max2 = Integer.MIN_VALUE; 
        int max3 = Integer.MIN_VALUE; 
        int max4 = Integer.MIN_VALUE; 

        for (int i = 0; i < arr.length; i++) { 
 
            if (arr[i] > max1) { 
 
                max4 = max3; 
                max3 = max2; 
                max2 = max1; 
                max1 = arr[i]; 
            } 

            else if (arr[i] > max2) { 
                max4 = max3; 
                max3 = max2; 
                max2 = arr[i]; 
            } 

            else if (arr[i] > max3) { 
                max4 = max3; 
                max3 = arr[i]; 
            } 

            else if (arr[i] > max4) 
                max4 = arr[i]; 
        } 
        return max1 + max2 + max3 + max4; 
    } 
 
    public static void main(String[] args) 
    { 
        int arr[] = { 2, 10, -4, 3, 14, 8 }; 
        System.out.println(findMaximumPairSum(arr)); 
    } 
}