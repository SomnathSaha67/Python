num=int(input("Enter a number to print its multiplication table: "))
end=int(input("Enter the end number for the multiplication table: "))
print(f"Multiplication table for {num}:")
for i in range(1,end+1):
    product=num*i
    print(f"{num} x {i} = {product}")
    i+=1
