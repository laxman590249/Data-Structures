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


print(longestArithSeqLength([3,6,9,12]))
# print(longestArithSeqLength([9,4,7,2,10]))
# print(longestArithSeqLength([20,1,15,3,10,5,8]))