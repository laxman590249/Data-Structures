

def find_missing(list_1: list, list_2: list):
    for number in list_2:
        list_1.remove(number)
    print(list_1)


def find_missing_2(list_1: list, list_2: list):
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    for number1, number2 in zip(list_1, list_2):
        if number1 != number2:
            return number1
    return list_1[-1]


print(find_missing_2([1,2,3,4,5,6,7],[3,7,2,1,4,6,5]))