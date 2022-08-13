x = (3, 2)
y = (-5, -10)
z = (-20, 5)


def choice(a, b, last=0):
    if a <= 0 or b <= 0:
        return -1
    fx = 0
    fy = 0
    fz = 0
    if last != 1:
        fx = 1 + choice(a+3, b+2, 1)
    if last != 2:
        fy = 1 + choice(a - 5, b - 10, 2)
    if last != 3:
        fz = 1 + choice(a - 20, b + 5)

    return max(fx, fy, fz)

print(choice(20, 1))