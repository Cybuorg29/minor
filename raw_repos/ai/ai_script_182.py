public class LongestString {
 
    public static String getLongestString(String[] array) {
    
        if(array.length == 0) {
            return null;
        }
         
        String longestString = array[0]; 
         
        for(int i = 1; i < array.length; i++) {
            if(array[i].length() > longestString.length()) {
                longestString = array[i];
            }
        }
         
        return longestString;
    }
    
    public static void main(String[] args) {
 
        String[] array = {"Google", "Facebook", "Amazon", "Zapier"};
         
        String longestString = getLongestString(array);
         
        System.out.println("Longest string: "+longestString); 
    }
}