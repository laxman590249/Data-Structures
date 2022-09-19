"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Solution:
1. We will have two pointers left, right
    we will keep left to less then the right one
    we will keep the profit
    if right is less then the left then we will make right to left and increase the right
    and every point we will keep track of max_porfit

2. Kadane's algo, we will keep track of sub array of maximum profit

    initialize max_array -> 0
    curr_max -> 0

    lopp 1 to N:
        max_array = max_array + arr[i] - arr[i-1]
        max_array = max(max_array, o)
        curr_max = max(curr_max, max_array)

"""