def get_permutations(string):
    n = len(string)
    result = []

    # Initialize a list to hold the characters of the string
    characters = list(string)

    while True:
        # Append the current permutation to the result
        result.append(''.join(characters))

        # Find the largest index i such that characters[i] < characters[i+1]
        i = n - 2
        while i >= 0 and characters[i] >= characters[i + 1]:
            print('came', i, characters)
            i -= 1

        # If no such index is found, we've generated all permutations
        if i == -1:
            break

        # Find the largest index j such that characters[j] > characters[i]
        j = n - 1
        while characters[j] <= characters[i]:
            j -= 1

        # Swap characters[i] and characters[j]
        characters[i], characters[j] = characters[j], characters[i]

        # Reverse the portion of the list to the right of i
        characters[i + 1:] = reversed(characters[i + 1:])
        print('Out', i, characters)

    return result


# Input string
input_string = input("Enter a string: ")

# Call the function to get and print permutations
permutations = get_permutations(input_string)
print("Permutations of the string:")
for perm in permutations:
    print(perm)





