public class LinearSearch 
{ 
    // This function returns index of element x in arr[] 
    static int search(int arr[], int x) 
    { 
        int n = arr.length; 
        for(int i = 0; i < n; i++) 
        { 
            if(arr[i] == x) 
                return i; 
        } 
        return -1; 
    } 
  
    public static void main(String args[]) 
    { 
        int arr[] = {23, 54, 12, 64, 76, 13, 45}; 
        int x = 45; 
  
        int index = search(arr, x); 
        if (index == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + index); 
    } 
}