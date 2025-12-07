def max_check(a,b):
    if a>b:
        return a
    else:
        return b
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print(f"The maximum of {num1} and {num2} is: {max_check(num1,num2)}")