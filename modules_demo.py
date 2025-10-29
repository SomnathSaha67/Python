#Import the random and math modules.
#Generate 10 random integers between 1 and 100.
#Calculate and print the average, minimum, and maximum using math where possible

import random
import math
# Generate 10 random integers between 1 and 100
random_integers = [random.randint(1, 100) for _ in range(10)]
# Calculate average, minimum, and maximum
average = sum(random_integers) / len(random_integers)
minimum = min(random_integers)
maximum = max(random_integers)
# Print the results
print(f"Random Integers: {random_integers}")
print(f"Average: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")




