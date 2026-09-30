#include<iostream> 
#include<vector> 
  
using namespace std; 


// Class to represent a Stack 
class Stack 
{
    // container to store elements 
    vector<int> v;    
    
public: 
    void push(int data); 
    bool empty(); 
    void pop(); 
    int top(); 
}; 

void Stack::push(int data) 
{ 
    // inserting an element 
    // on the top of the stack 
    v.push_back(data); 
} 

bool Stack::empty() 
{ 
    // checking if the stack is empty 
    return v.size() == 0; 
} 

void Stack::pop() 
{ 
    // removing element 
    // from the top of the stack 
    if (!empty()) 
    { 
        v.pop_back(); 
    } 
} 

int Stack::top() 
{ 
    // returns the top element 
    // of the stack 
    return v.back(); 
}