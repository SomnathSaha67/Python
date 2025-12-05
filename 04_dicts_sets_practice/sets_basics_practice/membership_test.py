set={1,2.0,3,4,5}
data=int(input("Enter an integer to check its membership in the set: "))
if data in set:
    print(f"{data} is present in the set")
else:
    print(f"{data} is not present in the set")