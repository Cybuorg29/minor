class MyClass
{
    public:
        bool isUpper(string str)
        {
            for(int i = 0; i < str.length(); i++)
            {
                if (islower(str[i])) 
                    return false; 
            }
            return true; 
        }
};