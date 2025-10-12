# polymorphism_demo.py

import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        """Method to calculate area — must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)
