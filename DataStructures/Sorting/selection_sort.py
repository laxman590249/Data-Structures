"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

> The subarray which is already sorted.
> Remaining subarray which is unsorted.

O(N2)

Default selection sort is unstable. We can make it stable by doing one small change,
if values are same then do not swap it

A sorting algorithm is said to be stable if two objects with equal or same keys appear in the same order in sorted
output as they appear in the input array to be sorted.

"""

list_1 = [60, 50, 40, 30, 20, 10]

for i in range(len(list_1)):
    min = i
    for j in range(i+1, len(list_1)):
        if list_1[min] > list_1[j]:
            min = j
    if min != i:
        list_1[min], list_1[i] = list_1[i], list_1[min]

print(list_1)

