class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vehicle:
    location = Point(0, 0)

    def __init__(self):
        pass

    def move(self, destination):
        self.location.x += destination.x
        self.location.y += destination.y

    def start(self):
        pass
    
class Car(Vehicle):
    def __init__(self, wheels):
        self.wheels = wheels

    def move(self, destination):
        print("Car with wheels {} will move to x={} y={}".format(self.wheels, destination.x, destination.y))
        super().move(destination)
        print("Move done")

# mazda = Car(wheels=4)
# mazda.move(Point(2, 2))
# print(mazda.location.x, mazda.location.y)