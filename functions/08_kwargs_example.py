def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
user_info(name="Bob", age=30, city="New York", profession="Engineer")
user_info(name="Eve", hobby="Painting", country="USA")
