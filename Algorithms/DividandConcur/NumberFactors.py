
numbers_can_used = [1, 3, 4]


def waysToGet(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    if n == 3:
        return 2

    substract_1 = waysToGet(n-numbers_can_used[0])
    substract_2 = waysToGet(n-numbers_can_used[1])
    substract_3 = waysToGet(n-numbers_can_used[2])

    return substract_1 + substract_2 + substract_3


print(waysToGet(10))