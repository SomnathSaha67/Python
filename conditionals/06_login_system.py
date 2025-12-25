username=input("Enter your username: ")
password=input("Enter your password: ")
is_authenticated="Login Successful" if username=="admin" and password=="password123" else "Login Failed"
print(is_authenticated)