

def power(n, x):
    if x == 1:
        return n
    return n * power(n, x-1)

print(power(3, 5))


"""
Calling the function for n/2

>  base log 2 N

"""

def power(n, x):
    if x == 0:
        return 1
    temp = power(n, x//2)
    if x % 2:
        return temp * temp * n
    else:
        return temp * temp

print(power(3, 10))