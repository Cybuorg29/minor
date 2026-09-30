public class TVShow {
  private String title; 
  private String network;
  private String genre;
  private int episodes;
  
  public TVShow(String t, String n, String g, int e) {
    title = t;
    network = n;
    genre = g;
    episodes = e;
  }
  
  public String getTitle() {
    return title;
  }
  
  public String getNetwork() {
    return network;
  }
  
  public String getGenre() {
    return genre;
  }
  
  public int getEpisodes() {
    return episodes;
  }
}