import os 
with open("tempfile.txt", "w") as file:
    file.write("This is a temporary file that will be deleted safely.\n")
def delete_file_safely(file_path):
    """Deletes the specified file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted successfully.")
    else:
        print(f"The file '{file_path}' does not exist.")
delete_file_safely("tempfile.txt")