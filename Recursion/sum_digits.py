


def sum_digits(n, sum = 0):

    if n <= 0:
        return sum
    else:
        return sum_digits(n//10, sum + (n%10))

print(sum_digits(1234))