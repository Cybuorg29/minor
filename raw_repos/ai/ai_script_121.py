class MyStack { 
    int top; 
    int capacity; 
    int stack[]; 
  
    // Creating stack 
    MyStack(int capacity) 
    { 
        this.capacity = capacity; 
        stack = new int[capacity]; 
        top = -1; 
    } 
  
    // Adding an element on top of the stack  
    public void push(int item) 
    { 
        if (top == capacity - 1){ 
            System.out.println("Stack overflow"); 
        } 
        else{ 
            stack[++top] = item; 
            System.out.println(item + " pushed into stack"); 
        } 
    } 
  
    // Removing an element from the stack 
    public int pop() 
    { 
        if (top == -1) { 
            System.out.println("Stack underflow"); 
            return 0; 
        } 
        else { 
            int item = stack[top--]; 
            return item; 
        } 
    } 
}