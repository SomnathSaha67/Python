def add(*args):
    return sum(args)
def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero."
        result /= num
    return result
print("Calculator Functions")
print("Addition: ", add(*map(int, input("Enter numbers separated by space: ").split())))
print("Subtraction: ", subtract(*map(int, input("Enter numbers separated by space: ").split())))
print("Multiplication: ", multiply(*map(int, input("Enter numbers separated by space: ").split())))
print("Division: ", divide(*map(int, input("Enter numbers separated by space: ").split())))