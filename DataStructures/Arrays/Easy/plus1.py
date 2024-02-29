"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


"""


def plus_one(digits):
    carry = 1
    result = []

    for digit in reversed(digits):
        total = digit + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result[::-1]


# Example usage
digits = [1, 2, 3]
result = plus_one(digits)
print(result)