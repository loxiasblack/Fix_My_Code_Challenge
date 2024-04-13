#!/usr/bin/python3
"""my square rectangle"""


class square():
    """square"""
    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Calculate the perimeter of the square."""
        return (4 * self.width)

    def __str__(self):
        """representaion of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=8)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
