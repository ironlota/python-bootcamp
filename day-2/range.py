l = [10, 11, 12]

a = [10, 11, 12, 14]
b = [13, 14, 15]

table = [
    [10, 11, 12, 14],     # 1
    [13, 14, 15],         # 2
    [16, 17, 18, 12, 14], # 3
    [19, 20, 21],         # 4
    [19, 20, 21],         # 5
    [19, 20, 21],         # 6
    [19, 20, 21],         # 7
]

print(len(table))

# i = row
# j = cols

# print([x for x in range(len(table))])
#    0   1   2
# 0  10  11  12
# 1  13  14  15
# 2  16  17  18

# range(0, len(table)) = [0, 1, ...., 3 - 1]

# range(0, 5) = [0, 1, 2, 3, 4]
# range(5) == range(0, 5) == [0, 1, 2, 3, 4]

# range(len(table)) = range(0, len(table))

# [0 ......... (len(table) - 1)]

for i in range(len(table)):
    # iterate rows
    # table[i] = row i
    print("Row " + str(i) + " = " + str(table[i]))
    for j in range(len(table[i])):
        # iterate cols
        # table[i][j] = cell at row i and col j
        print("Row " + str(i) + ", Col = " + str(j) + ", Element = " + str(table[i][j]))

