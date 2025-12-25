last_number=int(input("Enter the last number for the multiplication table: "))
for i in range(1, last_number + 1):
    for j in range(1, last_number + 1):
        print(f"{i} x {j} = {i * j:<3}", end=" ")
    print()
