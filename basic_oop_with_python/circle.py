import math

"""Class"""
class Circle():
    """Constructs a circle."""
    def __init__(self, radius):
        self.__radius = radius
        self.name = ""

    """Getter"""
    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_center(self):
        return self.coordinates

    def area(self):
        return math.pow(self.__radius, 2) * math.pi

    """Setter"""
    def set_color(self, color):
        self.__color = color

    def set_center(self, coordinates):
        self.coordinates = coordinates
