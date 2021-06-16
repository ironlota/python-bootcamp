lower_bound = int(input("Please input lower bound: "))
upper_bound = int(input("Please input upper bound: "))
num         = int(input("Please input number: "))

# TTTTTTTT lower_bound FFFFFFFF upper_bound TTTTTTT

if (num < lower_bound) or (num > upper_bound):
    print("Nice your num is fine!")
else:
    print("Damn, your num is bad mate!")