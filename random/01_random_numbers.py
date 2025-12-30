import random
start_int=int(input("Enter the start of the range for random integers: "))
end_int=int(input("Enter the end of the range for random integers: "))
num_of_integers=int(input("Enter the number of random integers to generate: "))
random_integers=[]
for _ in range(num_of_integers):
    rand_int=random.randint(start_int, end_int)
    random_integers.append(rand_int)
print(f"Random Integers between {start_int} and {end_int}: {random_integers}")
start_float=float(input("Enter the start of the range for random floats: "))
end_float=float(input("Enter the end of the range for random floats: "))
num_of_floats=int(input("Enter the number of random floats to generate: "))
random_floats=[]
for _ in range(num_of_floats):
    rand_float=random.uniform(start_float, end_float)
    random_floats.append(rand_float)
print(f"Random Floats between {start_float} and {end_float}: {random_floats}")
choices_list=input("Enter a list of items separated by commas for random choice: ").split(',')
print(f"List of items: {choices_list}")
num_of_choices=int(input("Enter the number of random choices to make from the list: "))
random_choices=[]
for _ in range(num_of_choices):
    choice=random.choice(choices_list)
    random_choices.append(choice)
print(f"Random Choices from the list: {random_choices}")
