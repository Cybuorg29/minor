def is_anagram(string, words) 
  words.each do |word|
    return true if word.split("").sort == string.split("").sort
  end
  return false
end