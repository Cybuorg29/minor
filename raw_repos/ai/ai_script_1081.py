import java.util.ArrayList;

public class GenerateStrings {

    public static ArrayList<String> generateStrings(int n){
        ArrayList<String> stringList = new ArrayList<>();
        
        char[] string = new char[n];
		generateStringUtil(string, n, 0, stringList);
		return stringList;
    }
    
    public static void generateStringUtil(char[] string, int n, int i, ArrayList<String> stringList){
        if(i == n){
            stringList.add(String.valueOf(string));
            return;
        }
        
        for(int j = 0; j < 10; j++){
            char c = (char) (j + '0'); 
            string[i] = c;
            generateStringUtil(string, n, i+1, stringList);
        }
    }
    
    public static void main(String[] args) {
        ArrayList<String> strings = generateStrings(3);
        System.out.println(strings);
    }
}