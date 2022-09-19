"""
Given length of wall w and shelves of two lengths m and n, find the number of each type of shelf to be used and the
remaining empty space in the optimal solution so that the empty space is minimum.
The larger of the two shelves is cheaper so it is preferred. However cost is secondary and first priority is to
minimize empty space on wall.

Input : w = 24 m = 3 n = 5
Output : 3 3 0

Input : w = 24 m = 4 n = 7
Output : 6 0 0

Approach:

1.



"""


def fitting_shelves(w, m, n):
    count = w//n
    min_rem = w
    solution = ''
    for i in range(count, -1, -1):
        number = i * n
        rem_number = w - number
        rem_2 = rem_number % m
        if rem_2 < min_rem:
            count_2 = rem_number // m
            solution = f"{count_2} {i} {rem_2}"
            min_rem = rem_2
            if rem_2 == 0:
                break
        # print(rem_number)

    return solution

print(fitting_shelves(30, 3, 5))
print(fitting_shelves(24, 4, 7))
print(fitting_shelves(29, 3, 9))






