import math

"""Class"""
class Square():
    """Constructs a square."""
    def __init__(self, side_length):
        self.__side_length = side_length

    """Getter"""
    def get_side_length(self):
        return self.__side_length

    def get_color(self):
        return self.__color

    def get_center(self):
        return self.coordinates

    def area(self):
        return self.__side_length * self.__side_length

    """Setter"""
    def set_color(self, color):
        self.__color = color

    def set_center(self, coordinates):
        self.coordinates = coordinates

    """Call the function and return the square."""
    def __str__(self):
        s = ""
        for j in range(0, self.__side_length):
            if j == 0 or j + 1 == self.__side_length:
                for i in range(0, self.__side_length):
                    s += "*"
                i = 0
            else:
                for i in range(0, self.__side_length):
                    if i == 0 or i + 1 == self.__side_length:
                        s += "*"
                    else:
                        s += " "
                i = 0
            if j + 1 != self.__side_length:
                s += "\n"
        return s
