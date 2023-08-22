"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Solution:

Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

We binary search the final result.
The left bound is max(A),
The right bound is sum(A).


https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/JavaC%2B%2BPython-Binary-Search


>>>

The key is left = max(weights), right = sum(weights),
which are the minimum and maximum possible weight capacity of the ship.

Therefore the question becomes Binary Search to find the minimum weight capacity of the ship between left and right.
We start from
mid = (left + right) / 2 as our current weight capacity of the ship.
need = days needed == 1
cur = current cargo in the ship == 0

Start put cargo into ship in order.
when need > D, it means the current ship is too small, we modify left = mid + 1 and continue
If all the cargo is successfully put into ships, we might have a chance to find a smaller ship, so let right = mid and continue.
Finally, when our left == right, we reach our answer

"""

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5


def shipWithinDays(weights, days):
    def is_feasible(capacity):
        days_needed, current_load = 1, 0

        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = 0
            current_load += weight

        return days_needed <= days

    left, right = max(weights), sum(weights)

    while left < right:
        mid = left + (right - left) // 2

        if is_feasible(mid):
            right = mid
        else:
            left = mid + 1

    return left

print(shipWithinDays(weights, days))


