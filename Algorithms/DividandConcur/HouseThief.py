

def max_money(house_worth, index):

    if index >= len(house_worth):
        return 0

    steal_current_house = house_worth[index] + max_money(house_worth, index+2)
    skip_current_house = max_money(house_worth, index + 1)

    return max(steal_current_house, skip_current_house)


print(max_money([6, 7, 1, 30, 18, 2, 4], 0))