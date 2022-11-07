"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4

s = "AABABBA", k = 1
Output: 4

Solution:


There's no edge case for this question. The initial step is to extend the window to its limit, that is, the longest
we can get to with maximum number of modifications. Until then the variable start will remain at 0.

Then as end increase, the whole substring from 0 to end will violate the rule, so we need to update start accordingly
(slide the window). We move start to the right until the whole string satisfy the constraint again.
Then each time we reach such situation, we update our max length.


"""


def longest_repeating(string, k):
    start = 0
    max_count = 0
    max_length = 0
    char_count = {}
    for index, char in enumerate(string):
        char_count[char] = char_count.get(char, 0) + 1
        max_count = max(max_count, char_count[char])
        while (index - start + 1 - max_count) > k:
            char_count[string[start]] = char_count.get(string[start], 0) - 1
            start += 1
        max_length = max(max_length, index-start+1)
    return max_length

print(longest_repeating('ABAB', 2))
print(longest_repeating('AABABBA', 1))
print(longest_repeating('AABABAAAAABBAAAA', 1))


