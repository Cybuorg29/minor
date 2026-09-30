def convert_integers_to_string(array)
  array.map(&:to_s).join(', ')
end

array = [1,2,3,4,5]
puts convert_integers_to_string(array)