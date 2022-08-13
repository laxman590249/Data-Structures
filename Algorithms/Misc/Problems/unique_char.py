
def unique_char_1(line: str):
    return len(set(str)) == len(str)


def unique_char(line: str):
    char_dict = {}
    for c in line:
        n = char_dict.get(c, 0)
        if n == 0:
            char_dict[c] = n+1
        else:
            return False
    return True


def unique_char_2(line: str):
    u = ''
    for c in line:
        if c in u:
            return False
        else:
            u += c
    return True


print(unique_char_2('aabcf'))
print(unique_char_2('abcf'))
