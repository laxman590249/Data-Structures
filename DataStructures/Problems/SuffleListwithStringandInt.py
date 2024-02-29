import random


def shuffle_with_constraints(lst):
    random.shuffle(lst)  # Shuffle the list randomly

    # Separate integers and strings
    integers = [item for item in lst if isinstance(item, int)]
    strings = [item for item in lst if isinstance(item, str)]

    shuffled = []

    while integers or strings:
        if len(shuffled) == 0 or (shuffled[-1] == 'int' and strings) or (shuffled[-1] == 'str' and integers):
            # If last item was an int and there are strings remaining, add a string
            # If last item was a string and there are integers remaining, add an int
            if shuffled and shuffled[-1] == 'int':
                shuffled.append(strings.pop(0))
            else:
                shuffled.append(integers.pop(0))
        else:
            # Otherwise, choose randomly between int and str
            if random.choice(['int', 'str']) == 'int' and integers:
                shuffled.append(integers.pop(0))
            elif strings:
                shuffled.append(strings.pop(0))

    return shuffled


# Example usage
original_list = [1, 'a', 2, 'b', 3, 'c', 4, 'd']
shuffled_list = shuffle_with_constraints(original_list)
print(shuffled_list)
