

def convert(s1, s2, i1, i2):

    if i1 == len(s1):
        return len(s2) - i2

    if i2 == len(s2):
        return len(s1) - i1

    if s1[i1] == s2[i2]:
        return convert(s1, s2, i1+1, i2 + 1)

    c1 = 1 + convert(s1, s2, i1+1, i2)
    c2 = 1 + convert(s1, s2, i1, i2+1)
    c3 = 1 + convert(s1, s2, i1+1, i2+1)

    return min(c1, c2, c3)


print(convert("Hello", "Hll", 0, 0))
