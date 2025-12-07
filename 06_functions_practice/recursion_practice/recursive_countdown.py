def countdown(n):
    if n<=0:
        print("Done!")
        return
    else:
        print(n)
        countdown(n-1)
num=int(input("Enter a number to start countdown: "))
countdown(num)