"""
Find all the subsets of the Array

{a, b, c}

Power Set:

{}, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}

Logic:

We will ask recursion to complete its own task then.
We will do our task like we will ask recursion to give power set of b,c and then we will attach a to it.

"""
power_s = []


def power_set_helper(list_obj, i):
    if i == len(list_obj)-1:
        return [[], [list_obj[i]]]
    partial_answer = power_set_helper(list_obj, i+1)
    final_answer = []
    for ans in partial_answer:
        final_answer.append(ans)
    for ans in partial_answer:
        temp = [list_obj[i]]
        temp.extend(ans)
        final_answer.append(temp)
    return final_answer


def power_set(list_obj):
    return power_set_helper(list_obj, 0)


print(power_set([1, 2, 3]))
