public class ArrayToString { 
    public static String convert(char[] arr) 
    { 
        StringBuilder sb = new StringBuilder(); 
        for (char c : arr) 
            sb.append(c); 
        return sb.toString(); 
    } 
  
    public static void main(String[] args) 
    { 
        char[] arr = { 'A', 'B', 'C', 'D' }; 
        System.out.println(convert(arr)); 
    } 
}