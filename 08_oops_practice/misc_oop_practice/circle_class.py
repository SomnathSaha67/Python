class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def circumference(self):
        import math
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius
number_of_circles = int(input("Enter number of circles: "))
circles = []
for _ in range(number_of_circles):
    radius = float(input("Enter radius of circle: "))
    circle = Circle(radius)
    circles.append(circle)
for circle in circles:
    print(f"\nCircle with radius: {circle.radius}")
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")
    print(f"Diameter: {circle.diameter():.2f}")