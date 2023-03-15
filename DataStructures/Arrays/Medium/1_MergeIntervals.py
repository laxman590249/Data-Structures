"""
Merge the interval if any interval is overlapping

Solution Without extra list:
Just sort it according to first interval
check the last of both if second interval is coming inside the interval

Solution Without extra list:
Just sort it according to first interval
check the last of both if second interval is coming inside the interval,
use here another list and use last element in the list to copmare the things

"""
list_obj = [[1, 2], [0, 3], [4, 5], [6, 7]]

list_result = sorted(list_obj, key=lambda i: i[0])
if len(list_result):
    prev = list_result[0]
    j = 1
    while j < len(list_result):
        if list_result[j][0] <= prev[1]:
            prev[1] = max(list_result[j][1], prev[1])
            list_result.pop(j)
        else:
            j += 1
        prev = list_result[j-1]
print(list_result)
