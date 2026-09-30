def sum_of_numbers
  total = 0 
  (1..10).each { |x| total += x }
  total
end

puts sum_of_numbers