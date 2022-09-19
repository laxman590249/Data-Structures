"""
Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Solution:

(https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas)

> If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
> If the total number of gas is bigger than the total number of cost. There must be a solution.

So we will start from starting

we will find at every station

tank = tank + gas[i] - cost[i]

If at any point tank is negative then we will have to say that won't be part of start index.

Find tank = tank + gas[i] - cost[i]
if tank < 0
    set total += tank
    set tank -> 0
    start += 1

in Last check, if tank + totol >= 0 then
    return start
    else
    return end
"""


class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        start = 0
        tank = 0
        total = 0
        count = len(gas)
        index = 0
        while index < count:
            tank = tank + gas[index] - cost[index]
            if tank < 0:
                total += tank
                tank = 0
                start = index + 1
            index += 1
        return -1 if (total + tank) < 0 else start


print(Solution().canCompleteCircuit(gas=[1,2,3,4,5] , cost=[3,4,5,1,2]))



