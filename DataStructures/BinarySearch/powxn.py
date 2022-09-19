"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Solution:

Recusrive Solution

"""



def find_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    return find_pow(x * x, n//2) if n % 2 == 0 else x * find_pow(x*x, n//2)

print(find_pow(3, -3))