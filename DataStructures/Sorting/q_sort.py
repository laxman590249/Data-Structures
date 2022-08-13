arr = [9, 4, 6, 3, 7, 1, 2, 11, 5]


def partiton(low, high):
    pivot = low
    while low < high:
        while arr[low] < arr[pivot]:
            low += 1
        while arr[high] > arr[pivot]:
            high -= 1
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
    temp = arr[high]
    arr[high] = arr[pivot]
    arr[pivot] = temp
    return high


def quick_sort(low, high):
    if low < high:
        pivot = partiton(low, high)
        quick_sort(low, pivot)
        quick_sort(pivot + 1, high)


quick_sort(0, len(arr)-1)
print(arr)