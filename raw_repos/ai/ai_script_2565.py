public class CountFrequency {
   static int countFrequency(String sentence, String word) 
    {
        int frequency = 0;
        String[] words = sentence.split(" ");
        for (String w : words) 
        {
            if (w.equals(word)) 
                frequency++; 
        }
        return frequency;
    }
    public static void main(String[] args) {
        String sentence = "I am learning to code";
        String word = "code";
        System.out.println(countFrequency(sentence,word));
    }
}