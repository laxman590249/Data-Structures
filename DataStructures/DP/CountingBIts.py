"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
1's in the binary representation of i.

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Solution:

In this we assume that all i%2 == 0 have the same number of one's in i/3
ex -- 4,2 have the same number of one's
if i==6 i/2 6/2 == 3
number of one's for six and three are equals
i%2 == 1;
we absorb the arr[i] = arr[i-1]+1;
for example t=if i == 5
ans = 2 no. of ones ,
ans[i] = arr[i-1]+1;
4 have only 1 one
1+1=2

"""


class Solution:

    def count_bits(self, n):
        result_list = [0] * (n+1)
        for i in range(1, n+1):
            if i % 2 == 0:
                result_list[i] = result_list[i//2]
            else:
                result_list[i] = result_list[i-1] + 1
        print(result_list)


Solution().count_bits(2)
Solution().count_bits(5)

