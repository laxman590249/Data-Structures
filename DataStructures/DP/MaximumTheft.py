""""
There are n houses build in a line, each of which contains some value in it. A thief is going to steal the maximal
value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his
two neighbors left and right side. What is the maximum stolen value?

Examples:

Input: hval[] = {6, 7, 1, 3, 8, 2, 4}
Output: 19

Solution:

We create a DP array,

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

Iterate dp -> 2 to n-1
    Everytime dp[i] = max(dp[i] + dp[i-2], dp[i-1])

"""