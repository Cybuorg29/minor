public class CommonChars {
    public static void main(String[] args) {
        String str1 = "abcde";
        String str2 = "defgh";
       
        //Loop through both strings
        for (int i = 0; i < str1.length(); i++) {
            char ch1 = str1.charAt(i);
            for (int j = 0; j < str2.length(); j++) {
                char ch2 = str2.charAt(j);
                
                // Compare characters
                if (ch1 == ch2) {
                    System.out.println(ch1);
                }
            }
        }
   }
}