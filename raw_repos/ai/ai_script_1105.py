public class Palindrome {
    public static boolean isPalindrome(String s) {
        int i = 0, j = s.length()-1; 
        while (i < j) { 
            if (s.charAt(i) != s.charAt(j)) 
                return false; 
            i++; 
            j--; 
        } 
  
        return true; 
    } 
 
    public static void main(String[] args) {
        String s = "madam";
        if (isPalindrome(s)) 
            System.out.println("The string is a palindrome."); 
        else
            System.out.println("The string is not a palindrome."); 
    }
 
}