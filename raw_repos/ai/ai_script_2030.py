import java.util.StringTokenizer; 

public class WordCounter 
{ 
    public static int countWords(String str) 
    { 
        StringTokenizer tokenizer = new StringTokenizer(str); 
        return tokenizer.countTokens(); 
    } 
  
    public static void main(String[] args) 
    { 
        String str = "Geeks for Geeks class"; 
        System.out.println("Number of words in a given String : " + countWords(str)); 
    } 
}