import random
num_dice=int(input("Enter the number of dice to roll: "))
dice_sides=int(input("Enter the number of sides on each die: "))
dice_results=[]
for _ in range(num_dice):
    roll=random.randint(1, dice_sides)
    dice_results.append(roll)
print(f"Dice roll results: {dice_results}")
#ASCII art for dice faces (1-6)
dice_art={
    1: ("┌─────┐\n"  
        "│     │\n"
        "│  ●  │\n"
        "│     │\n"
        "└─────┘"),
    2: ("┌─────┐\n"
        "│ ●   │\n"
        "│     │\n"
        "│   ● │\n"
        "└─────┘"),
    3: ("┌─────┐\n"
        "│ ●   │\n"
        "│  ●  │\n"
        "│   ● │\n"
        "└─────┘"),
    4: ("┌─────┐\n"
        "│ ● ● │\n"
        "│     │\n"
        "│ ● ● │\n"
        "└─────┘"),
    5: ("┌─────┐\n"
        "│ ● ● │\n"
        "│  ●  │\n"
        "│ ● ● │\n"
        "└─────┘"),     
    6: ("┌─────┐\n"
        "│ ● ● │\n"
        "│ ● ● │\n"     
        "│ ● ● │\n"
        "└─────┘")
}
print("ASCII Art for Dice Rolls:")
for result in dice_results:
    if result in dice_art:
        print(dice_art[result])
    else:
        print(f"Die with {result} sides rolled: {result} (No ASCII art available)")
    