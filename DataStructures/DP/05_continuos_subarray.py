"""



"""

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            print(hash_map)
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            # if the subarray size is at least two
            elif hash_map[s % k] < i:
                print(s % k)
                print(hash_map)
                return True
        print(hash_map)
        return False


print(Solution().checkSubarraySum([5,2,4,6,1], 6))
