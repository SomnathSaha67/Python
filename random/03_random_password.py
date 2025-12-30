import random
import string
length=int(input("Enter the desired length of the password: "))
include_uppercase=input("Include uppercase letters? (y/n): ").lower()=='y'
include_lowercase=input("Include lowercase letters? (y/n): ").lower()=='y'
include_digits=input("Include digits? (y/n): ").lower()=='y'
include_special=input("Include special characters? (y/n): ").lower()=='y'
character_pool=""
if include_uppercase:
    character_pool+=string.ascii_uppercase
if include_lowercase:
    character_pool+=string.ascii_lowercase
if include_digits:
    character_pool+=string.digits
if include_special:
    character_pool+=string.punctuation
if not character_pool:
    print("No character types selected. Cannot generate password.")
else:
    password="".join(random.choice(character_pool) for _ in range(length))
    print(f"Generated Password: {password}")