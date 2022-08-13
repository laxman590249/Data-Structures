
arr = [10, 5, 3, 15, 20]
arr.sort()


def find_largest_pair(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        j = i - 1
        while j >= 0:
            if not arr[i] % arr[j]:
                dp[i] = dp[i] + dp[j]
                # print(dp)
                break
            j -= 1
    max_value = max(dp)
    print(dp)
    print(max_value)
    i = len(arr)-1
    prev = arr[dp.index(max_value)]
    while i >= 0 and max_value:
        if dp[i] == max_value and prev % arr[i] == 0:
            print(arr[i], end=' ')
            max_value -= 1
            prev = arr[i]
        if max_value == 0:
            break
        i -= 1


find_largest_pair(arr)
