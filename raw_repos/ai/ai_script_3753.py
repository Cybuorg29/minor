def reverse_words(text):
  words = text.split(" ");
  reversedWords = words[::-1];
  return " ".join(reversedWords);