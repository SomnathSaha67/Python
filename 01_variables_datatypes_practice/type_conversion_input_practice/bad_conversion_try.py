string="abc"
try:
    number=int(string)
    print(f"Converted number: {number}, Type: {type(number)}")
except ValueError:
    print(f"Error: Cannot convert '{string}' to an integer.")