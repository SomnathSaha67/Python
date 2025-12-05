string=input("Enter any string including digits: ")
count=0
i=0
while i<len(digit):
    if digit[i].isdigit():
        count+=1
    i+=1
print(f"The number of digits in {digit} is {count}.")