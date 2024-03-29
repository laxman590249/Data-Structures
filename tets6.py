

class Solution:
    def minDifficulty(self, jobDifficulty: list, d: int) -> int:
        n = len(jobDifficulty)
        # Initialize the min_diff matrix to record the minimum difficulty
        # of the job schedule
        min_diff = [[float('inf')] * n + [0] for i in range(d + 1)]
        for days_remaining in range(1, d + 1):
            for i in range(n - days_remaining + 1):
                daily_max_job_diff = 0
                for j in range(i + 1, n - days_remaining + 2):
                    # Use daily_max_job_diff to record maximum job difficulty
                    daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j - 1])
                    min_diff[days_remaining][i] = min(min_diff[days_remaining][i],
                                                      daily_max_job_diff + min_diff[days_remaining - 1][j])
                print(days_remaining, min_diff)
        if min_diff[d][0] == float('inf'):
            return -1
        return min_diff[d][0]

print(Solution().minDifficulty([0, 1, 2, 3, 4, 5, 6], 3))