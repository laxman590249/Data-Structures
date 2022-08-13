

def knapsack_aux(profits, weights, capacity, current_index):

    if capacity <= 0 or current_index >= len(profits) or current_index < 0:
        return 0
    profit_1 = 0
    if weights[current_index] <= capacity:
        profit_1 = profits[current_index] +  knapsack_aux(profits, weights, capacity - weights[current_index], current_index + 1)
    profit_2 = knapsack_aux(profits, weights, capacity, current_index + 1)
    # print(profit_1, profit_2)
    return max(profit_1, profit_2)


print(knapsack_aux([31, 26, 72, 17], [3, 1, 5, 2], 7, 0))