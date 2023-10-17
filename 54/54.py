class Rectangle(): # 54.1
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getSquare(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

    def getRatio(self):
        return self.getSquare() / self.getPerimeter()

rectangle = Rectangle(10, 5)
print(rectangle.getSquare())
print(rectangle.getPerimeter())
print(rectangle.getRatio())