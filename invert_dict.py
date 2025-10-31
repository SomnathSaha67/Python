#Write a function to invert a dictionary (swap keys and values), assuming all the values are unique.

def invert_dict(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict[value] = key
    return inverted_dict        
# Example usage
original = {'a': 1, 'b': 2, 'c': 3}
inverted = invert_dict(original)
print("Original Dictionary:", original)
print("Inverted Dictionary:", inverted)