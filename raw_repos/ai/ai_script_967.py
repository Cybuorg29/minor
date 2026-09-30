public class BookCollection {
  private ArrayList<Book> books;
  private ArrayList<String> authors;

  public BookCollection() {
    this.books = new ArrayList<Book>();
    this.authors = new ArrayList<String>();
  }

  public void addBook(Book book) {
    this.books.add(book);
  }
  
  public void addAuthor(String author) {
    this.authors.add(author);
  }
  
  public ArrayList<Book> getBooks() {
    return this.books;
  }
  
  public ArrayList<String> getAuthors() {
    return this.authors;
  }
}