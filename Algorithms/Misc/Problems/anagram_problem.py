
# str_1 = input('Enter First String')
# str_2 = input('Enter Second Sting')

str_1 = 'Hello World'
str_2 = 'World Hello'


# Using Sorted Method
def anagram_test_1(string_1, string_2):
    str_1 = sorted(string_1.lower().replace(' ', ''))
    str_2 = sorted(string_2.lower().replace(' ', ''))
    return str_1 == str_2


#Manual Test
def anagram_test_2(string_1, string_2):
    string_1 = string_1.lower().replace(' ', '')
    string_2 = string_2.lower().replace(' ', '')

    if len(string_1) != len(string_2):
        return False

    dict_1 = dict()
    dict_2 = dict()

    for k in string_1:
        dict_1[k] = dict_1.get(k, 0) + 1

    for k in string_2:
        dict_1[k] = dict_1.get(k, 0) - 1

    for k in dict_1.keys():
        if dict_1.get(k, 0) != 0:
            return False
    return True


print(anagram_test_1(str_1, str_2))
print(anagram_test_2(str_1, str_2))
