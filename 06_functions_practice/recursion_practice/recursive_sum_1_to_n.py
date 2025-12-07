def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
num=int(input("Enter a number to calculate sum from 1 to n: "))
print(f"The sum of numbers from 1 to {num} is: {sum(num)}")