"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears
in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Input: s = "eccbbbbdec"
Output: [10]

Solution:

Traverse the string and find the maximum index of each character

Save right and check everytime if it is equal to that index



"""


def partition_labels(S):
    rightmost = {c: i for i, c in enumerate(S)}
    left, right = 0, 0
    print(rightmost)

    result = []
    for i, letter in enumerate(S):

        right = max(right, rightmost[letter])
        print(right, i, left)

        if i == right:
            result += [right - left + 1]
            left = i + 1

    return result

print(partition_labels("bbabcbacadefegdehijhklij"))


