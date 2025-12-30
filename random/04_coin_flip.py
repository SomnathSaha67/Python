import random
num_of_flips=int(input("Enter the number of coin flips to simulate: "))
results={"Heads":0, "Tails":0}
for _ in range(num_of_flips):
    flip=random.choice(["Heads", "Tails"])
    results[flip]+=1
print("Coin Flip Results after {} flips:".format(num_of_flips))
print("Heads: {}".format(results["Heads"]))
print("Tails: {}".format(results["Tails"]))
play_game=input("Do you want to play a coin flip guessing game? (y/n): ").lower()
if play_game=='y':
    user_guess=input("Heads or Tails? H/T: ").upper()
    flip=random.choice(["H", "T"])
    if user_guess==flip:
        print("You guessed correctly! It was {}.".format("Heads" if flip=="H" else "Tails"))
    else:
        print("Sorry, you guessed wrong. It was {}.".format("Heads" if flip=="H" else "Tails"))
else:
    print("Thank you for using the coin flip simulator!")