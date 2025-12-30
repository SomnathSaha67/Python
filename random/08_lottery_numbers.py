import random
lottery_numbers=[random.randint(1,49) for _ in range(6)]
your_number=int(input("Enter your lottery number (1-49): "))
print(f"Lottery Numbers: {lottery_numbers}")
if your_number in lottery_numbers:
    print("Congratulations! Your number is a winning number!")
else:
    print("Sorry, your number did not win this time.")