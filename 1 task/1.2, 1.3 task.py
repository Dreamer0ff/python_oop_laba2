class Car:
    color = "red" # цвет автомобиля
    fuel = 30 #количество топлива
    max_speed = 200
    type = "sedan"

    def print_properties(self):
        print("Color:", self.color)
        print("Fuel:", self.fuel)
        print("Max Speed:", self.max_speed)
        print("Type:", self.type)


car = Car()
car.print_properties()
