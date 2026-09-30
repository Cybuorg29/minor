class Student {
    private: 
        string name;
        int age;
        string gender;
    public: 
        Student(string name, int age, string gender)
            : name(name), age(age), gender(gender) { } 
            
        string getName() {
            return name;
        }
        
        int getAge() {
            return age;
        }
        
        string getGender() {
            return gender;
        }
};