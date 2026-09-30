def checkAlphabet(string): 

   alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

   for i in string: 
      if i not in alphabets: 
         return False
   return True