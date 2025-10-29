#Take a string input from the user.
#Print:
#The length of the string
#The first and last character
#The string in both uppercase and lowercase
#Check if the string is a palindrome (same forward and backward)

# Get user input
user_string = input("Enter a string: ") 
# Calculate required values
length = len(user_string)
first_char = user_string[0]
last_char = user_string[-1]
upper_case = user_string.upper()
lower_case = user_string.lower()
is_palindrome = user_string == user_string[::-1]
# Print the results
print(f"Length of the string: {length}")
print(f"First character: {first_char}")
print(f"Last character: {last_char}")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
print(f"Is palindrome: {is_palindrome}")

