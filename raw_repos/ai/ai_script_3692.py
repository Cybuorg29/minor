class Player {
    String name; 
    int age;
    String club;
    String position;

    // Constructors
    public Player(String name, int age, String club, String position) {
        this.name = name;
        this.age = age;
        this.club = club;
        this.position = position;
    }
    
    // Getters and Setters
    public String getName() {
        return this.name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return this.age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String getClub() {
        return this.club;
    }
    public void setClub(String club) {
        this.club = club;
    }
    public String getPosition() {
        return this.position;
    }
    public void setPosition(String position) {
        this.position = position;
    }
}