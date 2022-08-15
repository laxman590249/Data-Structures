"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is
quite high.

Complexity: O(N^2)

>>>
The above function always runs O(n^2) time even if the array is sorted.
It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap.

"""

list_1 = [60, 50, 40, 30, 20, 10]

for i in range(len(list_1)):
    for j in range(len(list_1)-i-1):
        if list_1[j] > list_1[j+1]:
            list_1[j+1], list_1[j] = list_1[j], list_1[j+1]

print(list_1)