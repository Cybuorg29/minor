def remove_special_chars(str)
   str = str.gsub(/[^a-zA-Z0-9\s]/, '')
   return str
end

puts remove_special_chars("Hello$#@World!")