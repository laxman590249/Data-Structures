

def sum_fun(n, sum = 0):
    if n <= 0:
        return sum
    else:
        return sum_fun(n-1, sum + n)

print(sum_fun(4))