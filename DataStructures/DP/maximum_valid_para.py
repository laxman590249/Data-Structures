data = """Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses  substring
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

"""


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_1 = 0
        count = 0
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')' and stack:
                if stack[-1] == '(':
                    count += 2
                    stack.pop()
                else:
                    count = 0
                if max_1 < count:
                    max_1 = count
        max_2 = 0
        count = 0
        if max_1 != len(s):
            stack = []
            for c in s[::-1]:
                if c == ')':
                    stack.append(')')
                elif c == '(' and stack:
                    if stack[-1] == ')':
                        count += 2
                        stack.pop()
                    else:
                        count = 0
                if max_2 < count:
                    max_2 = count
        print(max_1, max_2)
        return max_1 if max_1 <= max_2 and max_2 != 0 else max_2


print(Solution().longestValidParentheses(")()())"))
