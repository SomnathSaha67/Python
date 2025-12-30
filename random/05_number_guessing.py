import random
chances=5
print("Welcome to the Number Guessing Game!")
secret_number=random.randint(1, 100)
for attempt in range(1, chances+1):
    print("\nAttempt {} of {}:".format(attempt, chances))
    user_guess=int(input("Guess a number between 1 and 100: "))
    if user_guess < 1 or user_guess > 100:
        print("Your guess is out of bounds! Please guess a number between 1 and 100.")
    elif user_guess<secret_number:
        print("Too Low! Try again.")
    elif user_guess>secret_number:
        print("Too High! Try again.")
    else:
        print("Congratulations! You guessed the correct number: {}".format(secret_number))
        break
else:
    print("Sorry, you've used all your chances. The correct number was: {}".format(secret_number))
print("Thank you for playing the Number Guessing Game!")