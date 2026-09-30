nums = [1, 2, 3, 4, 5]

def sum_array(nums)
  sum = 0
  nums.each { |n| sum += n }
  return sum
end

puts sum_array(nums)