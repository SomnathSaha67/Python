digits=int(input("Enter a non-negative integer: "))
count_digits=str(digits)
sum_of_digits=0
stop=len(count_digits)
while stop > 0:
    digit=digits % 10
    sum_of_digits += digit
    digits //= 10
    stop -= 1
print(f"The sum of the digits is {sum_of_digits}.") 