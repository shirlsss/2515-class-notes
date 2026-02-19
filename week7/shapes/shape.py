import math

class Shape:
    def __init__(self, border_color, border_thickness, location):
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.location = location

    def __str__(self):
        return f"{self.__class__.__name__} ({self.border_color}, {self.border_thickness}, {self.location})"
    
    def change_border_color (self, color):
        self.border_color = color

class Circle(Shape):
    def __init__(self, radius, border_color, border_thickness, location):
        super().__init__(border_color, border_thickness, location)
        self.radius = radius
    
    def __str__(self):
        return f"{super().__str__()}, {self.radius}"
    
    def area(self):
        return math.pi * self.radius**2
        