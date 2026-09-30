public class FindIndex {
    public static int findIndex(int[] arr, int n) { 
        int i; 
        for (i = 0; i < arr.length; i++) { 
            if (arr[i] == n) 
                break; 
        } 
        if (i < arr.length) 
            return i; 
        else
            return -1; 
    } 
}