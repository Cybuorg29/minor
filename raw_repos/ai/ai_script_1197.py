def only_text(string)
  return string.gsub(/[0-9,]/, '')
end

only_text(string) // output: "This is a string with numbers such as  and  in it."