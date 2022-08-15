"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at
the correct position in the sorted part.

>> Basically, Insertion sort is efficient for small data values
>> Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.

Time Complexity: O(N^2)
Auxiliary Space: O(1)

"""




list_1 = [60, 50, 40, 30, 20, 10]

for i in range(len(list_1)):
    for j in range(i, 0, -1):
        if list_1[j] < list_1[j-1]:
            list_1[j-1], list_1[j] = list_1[j], list_1[j-1]


print(list_1)