import java.util.LinkedHashSet;

public class DuplicateWords {
    public static void findDuplicates(String str) {
        String[] words = str.split("\\s+");
        LinkedHashSet<String> set = new LinkedHashSet<>();
        for (int i = 0; i < words.length; i++) {
            if (!set.add(words[i])) {
                System.out.println(words[i]);
            }
        }
    }

    public static void main(String[] args) {
        String str = "He explained the problem in an intelligent and articulate manner.";
        findDuplicates(str);
    }
}

Output:
He
and