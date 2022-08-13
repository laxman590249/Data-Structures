"""
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store the first d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr_temp = {}
d = 3
for i in range(d):
    arr_temp[i] = arr[i]
l = 0
count = 0
length = len(arr)
while True:
    number = (l + d) % length
    if number in arr_temp:
        arr[l] = arr_temp[number]
    else:
        arr[l] = arr[number]
    count += 1
    l += 1
    if count >= len(arr):
        break
print(arr)





