class Circle():
    __radius = None
    def __init__(self, radius):
        self.__radius = radius

    def getSquare(self):
        return 3.14 * self.__radius ** 2

    def getCircumferenceLength(self):
        return 2 * 3.14 * self.__radius

circle = Circle(5)

print(circle.getSquare())
print(circle.getCircumferenceLength())