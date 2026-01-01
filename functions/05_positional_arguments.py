def display_info(name, age, city, profession):
    return f"{name}, aged {age}, lives in {city} and works as a {profession}."
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")
print(display_info(name, age, city, profession))