def generate_password(length):
  password = ""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  for i in range(length):
    password += choice(characters)
  return password

print(generate_password(10)) // output 5s@N#s9J@2