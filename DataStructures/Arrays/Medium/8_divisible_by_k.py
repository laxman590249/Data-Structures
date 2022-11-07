"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Solution:


"""

input = [60, 30, 150, 100, 40, 80, 120]

class Solution:
    def findDivisible(self, time):
        reminder = {}
        result = 0
        for t in time:
            if t % 60 == 0:
                result += reminder.get(0, 0)
            else:
                result += reminder.get(60-(t % 60), 0)
            reminder[t%60] = reminder.get(t%60, 0) + 1
        return result

print(Solution().findDivisible(input))


