def is_even(number):
    if number%2==0:
        return True
    else:
        return False
num=float(input("Enter a number: "))
print(f"Is the number {num} even? {is_even(num)}")