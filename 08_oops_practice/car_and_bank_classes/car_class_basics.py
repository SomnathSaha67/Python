class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage
    def drive_km(self,km):
        self.mileage+=km
        return self.mileage
number_of_cars=int(input("Enter number of cars: "))
cars=[]
for _ in range(number_of_cars):
    brand=input("Enter car brand: ")
    model=input("Enter car model: ")
    year=int(input("Enter car year: "))
    mileage=int(input("Enter car mileage: "))
    car=Car(brand, model, year, mileage)
    cars.append(car)
for car in cars:
    km=int(input(f"Enter kilometers driven for {car.brand} {car.model}: "))
    updated_mileage=car.drive_km(km)
    print(f"Updated mileage of {car.brand} {car.model}: {updated_mileage} km")