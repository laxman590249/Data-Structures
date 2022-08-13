list_1 = [60, 50, 40, 30, 20, 10]

for i in range(len(list_1)):
    for j in range(i, 0, -1):
        if list_1[j] < list_1[j-1]:
            list_1[j-1], list_1[j] = list_1[j], list_1[j-1]


print(list_1)