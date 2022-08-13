class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, val):
        self.width = val
    def set_height(self, val):
        self.height = val
    def get_area(self):
        return (self.width * self.height)
    def get_perimeter(self):
        return ((2 * self.width + 2 * self.height))
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ((("*" * self.width) + "\n") * self.height)
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    def __str__(self):
        return (("Rectangle(width={0}, height={1})").format(self.width, self.height))

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
    def set_side(self, val):
        self.side = self.width = self.height = val
    def set_width(self,value):
        self.set_side(value)
    def set_height(self,value):
        self.set_side(value)
    def __str__(self):
        return f'Square(side={self.side})'
