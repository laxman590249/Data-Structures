

array = [1, 3, 2, 2, 3, 1, 3, 1]


def array_sum(list, n):
    result_list = []
    for i in range(len(list)-1):
        for j in range(1, len(list)):
            if array[i]+array[j] == n:
                if array[i] < array[j]:
                    t = (array[i], array[j])
                else:
                    t = (array[j], array[i])
                if not t in result_list:
                    result_list.append(t)
    return result_list


def target_sum(list, k):
    if len(list) < 2:
        return
    seen = set()
    output = set()
    for num in list:
        target = k - num
        if target not in seen:
            seen.add(target)
        else:
            output.add((min(num, target), max(num, target)))
    return output


print(array_sum(array, 4))
print(target_sum(array, 4))


