public class ReverseString {
public void printReverseString(String s) {
 for(int i= s.length()-1; i>=0; i--) {
 char c = s.charAt(i);
 System.out.print(c);
 }
 System.out.println();
 }
}