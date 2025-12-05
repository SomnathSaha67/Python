n=int(input("Enter the last number n to sum from 1 to n: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f"The sum of numbers from 1 to {n} is {sum}.")