num=int(input("Guess the number (between 1 and 10): "))
secret_number=7
while num != secret_number:
    print("Wrong guess. Try again.")
    num=int(input("Guess the number (between 1 and 10): "))
print("Congratulations! You guessed the correct number.")