class Book {
   private int ISBN;
   private String title;
   private List<String> authors;
   private int year;
 
   public Book(int ISBN, String title, List<String> authors, int year) {
     this.ISBN = ISBN;
     this.title = title;
     this.authors = authors;
     this.year = year;
   }
   //getters and setters
 }