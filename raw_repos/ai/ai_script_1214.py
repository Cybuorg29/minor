public class TwoDArray{
    public static void print2DArray(int[][] arr){
        for (int[] row : arr){
            for (int element : row){
                System.out.print(element+" ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        int[][] arr = { {1,2,3}, {4,5,6}, {7,8,9} };
        print2DArray(arr);
    }
}