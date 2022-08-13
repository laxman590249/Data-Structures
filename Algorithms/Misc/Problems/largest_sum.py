

def largest_sum_1(list_1:list):
    if len(list_1) == 0:
        return 0

    max_sum = current_sum = list_1[0]
    for num in list_1[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

print(largest_sum_1( [-2,-1,-5,-18,-2,-2]))



