"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        res_index = -1
        current_index = 0
        needle_length = len(needle)

        if needle:
            start = 0
            expected_start = []
            haystack_len = len(haystack)
            needle_current = 0
            while start < haystack_len:
                if haystack_len[haystack_len] == needle[needle_current]:
                    if expected_start:
                        expected_start.append(start)

                start += 1
        else:
            res_index = 0

        return res_index