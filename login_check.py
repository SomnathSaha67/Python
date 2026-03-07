username= "admin"
password= 1234
ask_username= input("Enter username: ")
ask_password= int(input("Enter password: "))
if ask_username==username and ask_password==password:
  print("Login successful!")
else:
  print("Invalid credentials!")