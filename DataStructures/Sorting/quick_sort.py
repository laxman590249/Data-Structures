

L = [9, 4, 6, 3, 7, 1, 2, 11, 5]


def quick_sort_1(A, i, j, p):
    start = j
    while j <= p:
        if A[j] <= A[p]:
            i += 1
            A[j], A[i] = A[i], A[j]
        j += 1
    if p == 0 or p == i:
        return
    quick_sort_1(A, i, i+1, p)
    quick_sort_1(A, start-1, start, i-1)


def partition(A, p, q):
    pivot = q
    i = p-1
    for j in range(p, q+1):
        if A[j] <= A[pivot]:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def quick_sort_2(A, p, q):
    if p < q:
        r = partition(A, p, q)
        quick_sort_2(A, p, r-1)
        quick_sort_2(A, r+1, q)


quick_sort_2(L, 0, len(L)-1)
# quick_sort_1(L, -1, 0, len(L)-1)

print(L)



