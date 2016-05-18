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
        return self.center

    def area(self):
        return math.pow(self.__radius, 2) * math.pi

    """Setter"""
    def set_color(self, color):
        self.__color = color

    def set_center(self, center):
        self.center = center

    def intersection(self, c_bis):
        p1 = self.center
        p2 = c_bis.get_center()
        b = p2[1] - p1[1]
        a = p1[0] - p2[0]
        """Distance between two center points."""
        c = math.sqrt(a ** 2 + b ** 2)
        if c_bis.get_radius() + self.__radius < c:
            return False
        else:
            return True
