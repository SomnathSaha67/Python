correct_username=input("Enter your username: ")
correct_password=input("Enter your password: ") 
username=input("Username: ")
if username==correct_username or username!=correct_username:
    password=input("Password: ")
    if password==correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
