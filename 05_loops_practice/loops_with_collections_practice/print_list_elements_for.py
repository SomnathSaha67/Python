num_ele=int(input("Enter the number of elements in the list: "))
fruits=[]
for i in range(num_ele):
    fruit=input(f"Enter fruit {i+1}: ")
    fruits.append(fruit) 
print("The elements in the fruit list are:")
for fruit in fruits:
    print(fruit)