public class VowelCounter {

 public static int countVowels(String str) {
  int count = 0;
  for(int i = 0; i < str.length(); i++) {
   char currentChar = str.charAt(i);
   if(currentChar == 'a' || currentChar == 'e' || currentChar == 'i' || currentChar == 'o' || currentChar == 'u') {
    count++;
   }
  }
  return count;
 }

 public static void main(String[] args) {
  String str = "This is a test string";
  int count = countVowels(str);
  System.out.println("Number of vowels = " + count);
 }
}