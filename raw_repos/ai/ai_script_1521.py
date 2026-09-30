def fibonacci(n)
  if n < 2
    n
  else
    fibonacci(n-1) + fibonacci(n-2)
  end
end

1.upto(10) {|x| puts fibonacci(x)}