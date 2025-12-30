import random
options=["Rock", "Paper", "Scissors"]
num_of_rounds=int(input("Enter the number of rounds to play: "))
user_wins=0
computer_wins=0
for round_num in range(1, num_of_rounds+1):
    print("\nRound {}:".format(round_num))
    user_choice=input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    while user_choice not in options:
        user_choice=input("Invalid choice. Please enter Rock, Paper, or Scissors: ").capitalize()
    computer_choice=random.choice(options)
    print("Computer chose: {}".format(computer_choice))
    if user_choice==computer_choice:
        print("It's a tie!")
    elif (user_choice=="Rock" and computer_choice=="Scissors") or \
         (user_choice=="Paper" and computer_choice=="Rock") or \
         (user_choice=="Scissors" and computer_choice=="Paper"):
        print("You win this round!")
        user_wins+=1
    else:
        print("Computer wins this round!")
        computer_wins+=1
print("\nFinal Results after {} rounds:".format(num_of_rounds))
print("You won {} rounds.".format(user_wins))
print("Computer won {} rounds.".format(computer_wins))
if user_wins>computer_wins:
    print("Congratulations! You are the overall winner!")
elif computer_wins>user_wins:
    print("Computer is the overall winner! Better luck next time.")
else:
    print("The game ends in a tie!")
print("Thank you for playing Rock, Paper, Scissors!")