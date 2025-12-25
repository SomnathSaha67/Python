number_of_terms=int(input("Enter the number of terms in the Fibonacci sequence to generate: "))
if number_of_terms <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(number_of_terms):
        print(a)
        a, b = b, a + b