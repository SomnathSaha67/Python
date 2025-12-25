number=int(input("Enter a number greater than 0 to find its divisors: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(i)