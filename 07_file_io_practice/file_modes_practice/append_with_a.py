with open("log.txt","a") as file:
    file.write("Appending a new log entry using append mode 'a'.\n")
    file.write("Previous content remains intact.\n")
    file.write("This is useful for adding new information without deleting existing data.\n")
    file.write("End of appended log entry.\n")
with open("log.txt","r") as file:
    content=file.read()
print(content)