def multiplication_table(n, upto):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter the number to print its multiplication table: "))
upto = int(input("Enter the range up to which to print the table: "))
multiplication_table(num, upto)