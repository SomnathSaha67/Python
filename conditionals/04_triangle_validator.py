side1=float(input("Enter the length of side 1: "))  
side2=float(input("Enter the length of side 2: "))  
side3=float(input("Enter the length of side 3: "))
is_triangle="Valid Triangle" if side1+side2>side3 and side1+side3>side2 and side2+side3>side1 else "Invalid Triangle"
print(f"The triangle with sides {side1}, {side2}, and {side3} is a {is_triangle}.")