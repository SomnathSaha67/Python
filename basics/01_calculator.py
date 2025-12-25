operator=input("Enter the operation you want to perform (+, -, *, /): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
if operator=='+':
    result=num1+num2
    print(f"{num1} + {num2} = {result}")
elif operator=='-':
    result=num1-num2
    print(f"{num1} - {num2} = {result}")
elif operator=='*':
    result=num1*num2
    print(f"{num1} * {num2} = {result}")
elif operator=='/':
    if num2!=0:
        result=num1/num2
        print(f"{num1} / {num2} = {round(result, 3)}")
    else:
        print("Error: Division by zero is not allowed.")