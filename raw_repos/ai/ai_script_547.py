def squared(arr)
  result = []
  arr.each do |n|
    result << Math.sqrt(n)
  end
  result
end