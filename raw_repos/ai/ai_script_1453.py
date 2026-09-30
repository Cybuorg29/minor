public class Book { 
    // Properties 
    private String title; 
    private String author; 
    private int yearPublished; 
    
    // Constructors 
    public Book (String t, String a, int y) 
    { 
        title = t; 
        author = a; 
        yearPublished = y; 
    } 
    
    // Accessor and mutator methods 
    public void setTitle(String newTitle) { title = newTitle; } 
    public void setAuthor(String newAuthor) { author = newAuthor; } 
    public void setYearPublished(int newYear) { yearPublished = newYear; } 
    
    public String getTitle() { return title; } 
    public String getAuthor() { return author; } 
    public int getYearPublished() { return yearPublished; } 
}