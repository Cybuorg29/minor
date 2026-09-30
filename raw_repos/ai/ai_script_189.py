class Person {
    string name;
    int age;
    string address;
 
public:
    Person();
    Person(string name, int age, string address);
 
    string getName();
    int getAge();
    string getAddress();
 
    void setName(string name);
    void setAge(int age);
    void setAddress(string address);
};