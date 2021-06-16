# mesin
# roda
# dashboard
# warna

# maju / mundur .... (vector)
# ngerem

class Car: # ini cetakan mobil, blm implementasi mobil nya
    warna = 'merah-biru'
    roda  = 4
    mesin = 'v8'

    def maju(self):
        self.printInfo()
        print('mobil berwarna ' + self.warna + ' ini sedang melaju')

    def printInfo(self):
        print('Warna = {}, Roda = {}, Mesin = {}'.format(self.warna, self.roda, self.mesin))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distancePoint(self, destination):
#         return Point(abs(destination.x - self.x), abs(destination.y - self.y))


# point1 = Point(2, 3)
# point2 = Point(4, 5)

# distance = point1.distancePoint(point2)
# print(distance.x, distance.y)

# constructor
# how the implementation of the blueprint is constructed (denotes as `__init__` )
# parameters of the constructor denote as "requirements" of the implementation itself

class Food:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def decrease(self):
        if (self.amount > 0):
            self.amount = self.amount - 1
        else:
            print('The food is empty')

    def increase(self):
        self.amount = self.amount + 1

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def ditusukDariBelakang(self, person):
        print('Wah, saya yg bernama {} dan gender {}, ditusuk oleh orang yang bernama {} dan gender {}'.format(self.name, self.gender, person.name, person.gender))
        print('Sakit bgt')

    def makan(self, food):
        if (food.amount > 0):
            print('Saya yang bernama {} memakan {}'.format(self.name, food.name))
            food.decrease()
        else:
            print('{} ga bisa makan makanan yg kosong'.format(self.name))

# ray = Human('ray', 'laki')
# pizza = Food('pizza', 7)

# print('Ada {} pizza'.format(pizza.amount))
# ray.makan(pizza)
# print('Sekarang ada {} pizza'.format(pizza.amount))

