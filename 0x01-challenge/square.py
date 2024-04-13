#!/usr/bin/python3
"""my square rectangle"""


class square():
    """square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """instantiation"""
        if (kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """the perimetre of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """representaion of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
