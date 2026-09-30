def fibonacci(limit)
  n1, n2 = 0, 1
  puts "Fibonacci series upto #{limit}"
  while n1 <= limit
    print "#{n1}, "
    n1, n2 = n2, n1 + n2
  end
end

fibonacci(20)