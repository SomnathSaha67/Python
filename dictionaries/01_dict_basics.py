#Create, access, add, update, delete key-value pairs in a dictionary and display the final dictionary
my_dict1 = {}
num_pairs=int(input("Enter number of key-value pairs you want to add to the dictionary: "))
for i in range(num_pairs):
    key=input("Enter key {}: ".format(i+1))
    value=float(input("Enter value for key '{}': ".format(key)))
    my_dict1[key]=value
print("Original Dictionary: ", my_dict1)
# Update a value
update_key=input("Enter the key of the value you want to update: ")
if update_key in my_dict1:
    new_value=float(input("Enter the new value for key '{}': ".format(update_key)))
    my_dict1[update_key]=new_value
    print("Dictionary after updating key '{}': {}".format(update_key, my_dict1))
else:
    print("Key '{}' not found in the dictionary.".format(update_key))
my_dict2={}
num_pairs2=int(input("Enter number of key-value pairs you want to add to the second dictionary: "))
for i in range(num_pairs2):
    key=input("Enter key {}: ".format(i+1))
    value=float(input("Enter value for key '{}': ".format(key)))
    my_dict2[key]=value
print("Second Dictionary: ", my_dict2)
# Merge two dictionaries
my_dict1.update(my_dict2)
print("Dictionary after merging with second dictionary: ", my_dict1)
# Delete a key-value pair
delete_key=input("Enter the key you want to delete: ")
if delete_key in my_dict1:
    del my_dict1[delete_key]
    print("Dictionary after deleting key '{}': {}".format(delete_key, my_dict1))
else:
    print("Key '{}' not found in the dictionary.".format(delete_key))
print("Final Dictionary: ", my_dict1)
# Accessing values
access_key=input("Enter the key whose value you want to access: ")
if access_key in my_dict1:
    print("Value for key '{}': {}".format(access_key, my_dict1[access_key]))
else:
    print("Key '{}' not found in the dictionary.".format(access_key))
print("All Keys: ", list(my_dict1.keys()))
print("All Values: ", list(my_dict1.values()))
print("All Key-Value Pairs: ", list(my_dict1.items()))