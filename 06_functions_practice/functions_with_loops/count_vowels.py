def count_vowles(string):
    count=0
    vowels='aeiouAEIOU'
    for char in string:
        if char in vowels:
            count+=1
    return count
input_string=input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowles(input_string)}