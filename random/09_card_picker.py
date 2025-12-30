import random
suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck=[f"{rank} of {suit}" for suit in suits for rank in ranks]
print("Deck of Cards:")
for card in deck:                   
    print(card)
num_of_picks=int(input("Enter the number of random cards to pick from the deck: "))
picked_cards=[]
for _ in range(num_of_picks):
    card=random.choice(deck)
    picked_cards.append(card)
print(f"Picked Cards: {picked_cards}")
