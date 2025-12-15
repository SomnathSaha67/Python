class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def display(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}, Area: {self.area()}, Perimeter: {self.perimeter()}")
number_of_rectangles = int(input("Enter number of rectangles: "))
rectangles = []
for _ in range(number_of_rectangles):
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    rectangle = Rectangle(length, breadth)
    rectangles.append(rectangle)
for rectangle in rectangles:
    rectangle.display()
