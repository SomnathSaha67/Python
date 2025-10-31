#Take a sentence as input.
#Count and print the frequency of each word using a dictionary.

# Taking a sentence as input
sentence = input("Enter a sentence: ")
# Splitting the sentence into words
words = sentence.split()
# Creating a dictionary to store word frequencies
word_frequency = {}
# Counting the frequency of each word
for word in words:
    word = word.lower()  # Convert to lowercase for uniformity
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
# Printing the frequency of each word
print("\nWord Frequency:")
for word, frequency in word_frequency.items():
    print(f"'{word}': {frequency}")