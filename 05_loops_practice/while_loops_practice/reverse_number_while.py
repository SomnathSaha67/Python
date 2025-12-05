num=input("Enter a number to reverse: ")
print(f"The original number is: {num}")
reversed_num=""
i=len(num)-1
while i>=0:
    reversed_num+=num[i]
    i-=1
print(f"The reversed number is: {reversed_num}")