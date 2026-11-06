table = [1,2,3,4,5,6]

for i in range(0,(len(table)) // 2):

    temp = table[i]
    table[i] = table[len(table) -1 -i]
    table[len(table) -1 - i] = temp

print(table)