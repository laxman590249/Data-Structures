

"""
Recursion tree is representing the Recursion according to its inputs.
"""


"""
Recursion tree for below function:

5 -> 4 -> 3 -> 2 -> 1 

O(N)

"""

def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n-1)

print(sum_n(5))


"""
Recursion tree for below function:

See document

O(N)

"""

def fibo(n):
    print(n)
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(7))


