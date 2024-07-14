import math
class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width
    
    def set_width(self, width):
        self.width = width

    def get_area(self):
        return (self.height * self.width)
    
    def get_perimetr(self):
        return (2 * (self.height + self.width))
    
    def get_info(self):
        area = self.get_area()
        perimeter = self.get_perimetr()
        return (f"Rectangle info:\n"f"Height: {self.height}\n"f"Widtg: {self.width}\n"f"Area: {area}\n"f"Perimeter: {perimeter}" )
    

rectangle1 = Rectangle(5, 7)

print(rectangle1.get_info())

rectangle1.set_height(10)
rectangle1.set_width(12)

print(rectangle1.get_info())