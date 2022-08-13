"""

A[9, 3, 7, 5, 6, 4, 8, 2]

- Recursive Procedure
- It follows the divide and concur

"""


a = [9, 3, 7, 5, 6, 4, 8, 2]


def mergeSort(arr):
    length = len(arr)
    if len(arr) > 1:
        mid = length//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1


mergeSort(a)
print(a)