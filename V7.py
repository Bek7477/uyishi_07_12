import math

class Circle:
    def __init__(self, radius, color) -> None:

        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
    def get_info(self):
        area = self.get_area()
        circumference = self.get_circumference()
        return (f"Circle info: \n"f"Radius: {self.radius}\n"f"Color: {self.color}\n"f"Area: {area:.2f}\n"f"Cercumference: {circumference:.2f}")
    
circle1 = Circle(5, "Red")
print(circle1.get_info())
print("")
circle1.set_radius(10)
circle1.set_color("Blue")

print(circle1.get_info())
                
    