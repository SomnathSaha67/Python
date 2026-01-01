gender = input("Enter your gender (M/F): ")
match gender:
    case "":
        print("No gender provided.")
    case "M" | "m":
        print("Male")
    case "F" | "f":
        print("Female")
    case _:
        print("Other")
