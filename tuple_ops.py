#Ask the user for two tuples (input as comma-separated values).
#Convert input strings to tuples, concatenate them, and print the result.

# Get user input for two tuples
tuple1_input = input("Enter the first tuple (comma-separated values): ")
tuple2_input = input("Enter the second tuple (comma-separated values): ")
# Convert input strings to tuples
tuple1 = tuple((item.strip() for item in tuple1_input.split(',')))
tuple2 = tuple((item.strip() for item in tuple2_input.split(',')))
# Concatenate the tuples
concatenated_tuple = tuple1 + tuple2
# Print the result
print(f"Concatenated Tuple: {concatenated_tuple}")