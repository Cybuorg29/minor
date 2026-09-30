def extract_verbs(sentence):
  verbs = []
  words = sentence.split(" ")
  for w in words:
    if w.endswith("ed") or w.endswith("ing"):
      verbs.append(w)
  return verbs