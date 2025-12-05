limit=int(input("Enter the upper limit to print odd numbers: "))
print(f"Printing odd numbers from 1 to {limit}, skipping even numbers:")
for i in range(1, limit + 1):
    if i % 2 == 0:
        continue
    print(i)