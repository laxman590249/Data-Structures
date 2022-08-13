

string = 'Hello'

def reverse(string , result = ''):
    if len(string) <= 0:
        return result
    else:
        result = string[0] + result
        return reverse(string[1:], result)

def reverse_1(s):
    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]

print(reverse(string))
print(reverse_1(string))