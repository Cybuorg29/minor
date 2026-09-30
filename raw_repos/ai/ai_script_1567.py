class Student {
  private:
    string name;
    int age;
    string address;
  public:
    Student();
    Student(string name, int age, string address);
    void setName(string name);
    void setAge(int age);
    void setAddress(string address);
    string getName();
    int getAge();
    string getAddress();
};