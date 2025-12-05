num=int(input("Enter the number to find its first multiple: "))
i=1
while True: 
    if i%num==0:
        multiple=i
        print(f"The first multiple of {num} is {multiple}.")
        break
    i+=1