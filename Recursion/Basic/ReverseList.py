list_obj = [1, 2, 3, 4, 5]


def reverse(l, r, list_obj):
    if l >= r:
        return
    list_obj[l], list_obj[r] = list_obj[r], list_obj[l]
    reverse(l+1, r-1, list_obj)


reverse(0, len(list_obj)-1, list_obj)
print(list_obj)