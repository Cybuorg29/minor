public class ReverseList {
    public static void reverseList(List<String> list) 
    {
        if (list.size() > 1) {
            String temp = list.get(0);
            list.remove(0);
            reverseList(list);
            list.add(temp);
        }
    }

    public static void main(String[] args) 
    { 
        List<String> list = new ArrayList<String>(Arrays.asList("John", "Alice", "Bob"));
        reverseList(list);
        System.out.println(list); 
    } 
}