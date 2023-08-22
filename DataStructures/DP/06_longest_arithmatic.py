""""

"""


def longestArithSeqLength( A):
    dp = {}
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
            print(dp)
    print(dp)
    return max(dp.values())


print(longestArithSeqLength([10,9,2,5,3,7,101,18]))
# print(longestArithSeqLength([9,4,7,2,10]))
# print(longestArithSeqLength([20,1,15,3,10,5,8]))