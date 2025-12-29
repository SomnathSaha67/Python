board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append('-')  # Initialize empty cell
    board.append(row)
for row in board:
    print(" ".join(row))
# Displaying the tic-tac-toe board  
print("Tic-Tac-Toe Board:")
for row in board:
    print(" | ".join(row))
    print("-" * 9)
