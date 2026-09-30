def sum_odd_numbers(start, finish)
  total = 0
  (start..finish).each do |number|
    total += number if number % 2 == 1 
  end
  total
end

p sum_odd_numbers(1, 10)