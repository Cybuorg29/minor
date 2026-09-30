# Function to return the nth Fibonacci number 
def calculateFibonacci(num) 
  if num < 0 
    return 'Incorrect input'
  elsif num == 0 
    return 0 
  elsif num == 1 
    return 1 
  end
  #Recursive Function 
  return calculateFibonacci(num - 1) +  calculateFibonacci(num - 2) 
end 
  
# Driver Program 
puts calculateFibonacci(7)