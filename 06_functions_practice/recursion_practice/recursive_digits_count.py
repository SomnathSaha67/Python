def digits_count(n):
    if n<10:
        return 1
    else:
        return 1+digits_count(n//10)
num=int(input("Enter a non-negative integer to count its digits: "))
print(f"The number of digits in {num} is: {digits_count(num)}")