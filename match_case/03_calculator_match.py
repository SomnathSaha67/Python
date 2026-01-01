operation=input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        operands = input("Enter numbers to add, separated by spaces: ")
        numbers = list(map(float, operands.split()))
        result = sum(numbers)
        print(f"Result: {result}")
    case "-":
        operands = input("Enter numbers to subtract, separated by spaces: ")
        numbers = list(map(float, operands.split()))
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"Result: {result}")
    case "*":
        operands = input("Enter numbers to multiply, separated by spaces: ")
        numbers = list(map(float, operands.split()))
        result = 1
        for num in numbers:
            result *= num
        print(f"Result: {result}")
    case "/":
        operands = input("Enter numbers to divide, separated by spaces: ")
        numbers = list(map(float, operands.split()))
        result = numbers[0] 
        for num in numbers[1:]:
            if num == 0:
                print("Error: Division by zero.")
                break
            result /= num
        else:
            print(f"Result: {result}")
    case _:
        print("Invalid operation.")
