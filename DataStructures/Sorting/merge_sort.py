"""
The Merge Sort algorithm is a sorting algorithm that is considered an example of the divide and conquer strategy.
So, in this algorithm, the array is initially divided into two equal halves and then they are combined in a
sorted manner. We can think of it as a recursive algorithm that continuously splits the array in half until it cannot
be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop,
i.e. it is the base case to stop the recursion.


A[9, 3, 7, 5, 6, 4, 8, 2]

- Recursive Procedure
- It follows the divide and concur

Time Complexity: O(n log(n)),
Auxiliary Space: O(n)


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