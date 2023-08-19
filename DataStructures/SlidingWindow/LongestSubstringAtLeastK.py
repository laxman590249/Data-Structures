"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of
each character in this substring is greater than or equal to k.

Input: s = "aaabb", k = 3
Output: 3

Input: s = "ababbc", k = 2
Output: 5

Solution:

Two pointer approach

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87739/Java-Strict-O(N)-Two-Pointer-Solution

"""
import collections
