#include <iostream> 
using namespace std; 
  
int max_sum(int arr[], int n) 
{ 
    if (n == 0) 
        return 0; 
        
    int max = arr[0]; 
    int sum = arr[0]; 
  
    for (int i = 1; i < n; i++) { 
  
        if (arr[i] < 0) 
            return 0; 
            
        sum = max(sum + arr[i], arr[i]); 
        max = max(max, sum); 
    } 
  
    return max; 
} 
///
16. Instruction: Create a function in Python that returns the number of times a given substring occurs in a string.
16. Input:
string = "Hello, Hello, Hello!"
substring = "Hello"
16. Output:
def count_substring(string, substring): 
  
    count = 0
  
    #Loop through the string 
    for i in range(0, len(string)): 
        if (string[i:i+len(substring)] == substring): 
            count += 1
 
    return count