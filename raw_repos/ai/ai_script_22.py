The efficient way to sort the array using Java is to use the Quicksort algorithm which is an in-place, recursive sorting algorithm with an average time complexity of O(n log n). The Quicksort algorithm works by selecting an element as a pivot, partitioning the array around the pivot, and recursively applying the Quicksort algorithm to the two sub-arrays on either side of the pivot. This process continues until all the elements in the array are sorted.

The code for the Quicksort algorithm in Java will look something like this:

public class QuickSort {
    // Method for rearranging the elements
    public static void sort(int[] arr, int low, int high) {
        // Check for base case
        if (low < high) {
            int pi = partition(arr, low, high);
            // Recursively sort elements before
            // partition and after partition
            sort(arr, low, pi-1);
            sort(arr, pi+1, high);
        }
    }

    // Method for partitioning the array on the basis of the pivot
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            // If the current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;

                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i + 1] and arr[high] (or pivot)
        int temp2 = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp2;

        return i + 1;
    }
}