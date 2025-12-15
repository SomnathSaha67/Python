class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
    def current_year(self,current_year):
        return current_year - self.year()
    def print_details(self):
        print(f"Car Details - Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage} km")
number_of_cars = int(input("Enter number of cars: "))
cars = []
for _ in range(number_of_cars): 
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    mileage = int(input("Enter car mileage: "))
    car = Car(brand, model, year, mileage)
    cars.append(car)
for car in cars:    
    car.print_details()
    current_year = int(input(f"Enter current year to calculate age of {car.brand} {car.model}: "))
    age = car.current_year(current_year)
    print(f"Age of {car.brand} {car.model}: {age} years")
