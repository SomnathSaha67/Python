character=input("Enter a single character: ")
vowel_consonant="Vowel" if character in 'aeiouAEIOU' else "Consonant"
print(f"The character '{character}' is a {vowel_consonant}.")