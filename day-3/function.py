# f(x) = y = ax + b
# log(x)

# Luas(sisi) = sisi x sisi
# Luas(panjang, lebar) = panjang * lebar

# inputs dalam function dibilang arguments / parameters

# def luasPersegi(sisi):
#     return sisi * sisi # return value

def printLuasPersegi(sisi): 
    print(sisi * sisi) # no return value (no output)

# def luasPersegiPanjang(panjang, lebar):
#     return panjang * lebar

def printLuasPersegiPanjang(panjang, lebar):
    print(panjang * lebar)

# f(g(x))
# y = g(x)
# f(y)

# we have square 
# side = root of 5

# kita hanya bisa masukkin angka dari 1 - 10
# luas persegi yang sisinya 100

# clue use 2 functions
def square(num):
    return num * num

def squareThenTimesThree(num):
    return square(num) * 3

def addThree(num):
    num += 3

def printValue():
    value = 4
    addThree(value)
    print(value)

def sum3Values(num1, num2, num3):
    return num1 + num2 + num3

def luasPersegiPanjang(panjang, lebar):
    return panjang * lebar

# print(luasPersegiPanjang(lebar=10, panjang=5))
# print(luasPersegiPanjang(panjang=5, lebar=10))
# print(luasPersegiPanjang(5, 10))

def countLuas():
    def luasPersegi(sisi):
        return sisi * sisi

    a = [1,2,3,4,5,6,7,8,9,10]
    for val in a:
        luasPersegi(val)

# countLuas()

# luasPersegi(10)

# f(x) = x
# luasPersegi(sisi)

# buat function yang bisa print every elements in a list
def printList(l):
    for element in l:
        print(element)

# printList(['ade', 'ray', 'nathan'])
# printList('rayandrew')

# buat sebuah fungsi
# yang menerima parameter:
# 1. Waktu kerja (hour)
# 2. Pay per hour
# Print berapa hasil pendapatan sebuah pekerja jika dikurangi tax 10%

def gaji(waktu, rate):
    gross_salary = waktu * rate
    nett_salary  = 90 / 100 * gross_salary
    print(nett_salary)

def gaji2(time, pay):
    payment = time * pay
    return payment - (payment * 0.1)