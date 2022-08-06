"""


"""


s = "kadak"


def palindrom(l, r, s):
    if l >= r:
        return True
    if s[l] == s[r]:
        return palindrom(l+1, r-1, s)
    else:
        return False

print(palindrom(0, len(s)-1, s))




