list_1 = [60, 50, 40, 30, 20, 10]

for i in range(len(list_1)):
    min = i
    for j in range(i+1, len(list_1)):
        if list_1[min] > list_1[j]:
            min = j
    if min != i:
        list_1[min], list_1[i] = list_1[i], list_1[min]

print(list_1)

