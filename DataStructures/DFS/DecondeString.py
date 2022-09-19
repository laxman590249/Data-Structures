"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

"""
# s = "3[a]2[bc]"
s = "3[a2[c]]"
stack = []
string_result = ''
for i in s:
    if i.isdigit():
        stack.append(int(i))
        continue
    if i == ']':
        string_stack = stack.pop()
        stack.pop()
        count = stack.pop()
        string_stack = str(string_stack) * int(count)
        print(string_stack, count)
        if len(stack) != 0:
            stack.append(stack.pop() + string_stack)
        else:
            string_result += string_stack
    else:
        if len(stack) > 0:
            if stack[-1] == '[' or i == '[':
                stack.append(i)
            else:
                el = stack.pop()
                el = el + i
                stack.append(el)
        else:
            stack.append(i)

    print(stack)
print(string_result)

