a = input("Enter value for a: ")
b = input("Enter value for b: ")
print("Before Swapping: a =", a, ", b =", b)
a, b = b, a  # Tuple unpacking to swap values
print("After Swapping: a =", a, ", b =", b)