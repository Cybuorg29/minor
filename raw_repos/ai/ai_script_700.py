class NewsSystem {
    public string title;
    public string content;
    
    public NewsSystem(string title, string content) {
        this.title = title;
        this.content = content;
    }
}

interface INewsActions {
    void PostNewArticle(NewsSystem article);
    void EditArticle(NewsSystem article);
    void DeleteArticle(NewsSystem article);
}