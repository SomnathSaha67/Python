#Prompt the user for a list of numbers (entered separated by spaces).
#Print the max, min, sum, and average.
#Sort and reverse the list, displaying each result.

# Get user input
user_input = input("Enter a list of numbers separated by spaces: ")
# Convert input string to a list of floats
number_list = [float(num) for num in user_input.split()]
# Calculate max, min, sum, and average
maximum = max(number_list)
minimum = min(number_list)
total_sum = sum(number_list)
average = total_sum / len(number_list)
# Sort and reverse the list
sorted_list = sorted(number_list)
reversed_list = list(reversed(sorted_list))
# Print the results
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Sorted List: {sorted_list}")
print(f"Reversed List: {reversed_list}")