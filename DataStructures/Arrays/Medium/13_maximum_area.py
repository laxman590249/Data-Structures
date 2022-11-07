"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

Solution:

We have to find max horizontal cut  and vertical cut
max piece will be multiplication of both

"""

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]

class Solution:
    def find_max_cake(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        max_cut = 0
        h_last = 0
        v_last = 0
        max_h_cut = 0
        h_last = 0
        for h_value in horizontalCuts:
            max_h_cut = max(max_h_cut, h_value-h_last)
            h_last = h_value
        max_v_cut = 0
        v_last = 0
        for v_value in verticalCuts:
            max_v_cut = max(max_v_cut, v_value - v_last)
            v_last = v_value
        print(max_v_cut * max_h_cut)

        # for h_value in horizontalCuts:
        #     h_cut = h_value - h_last
        #     v_last = 0
        #     for v_value in verticalCuts:
        #         v_cut = v_value - v_last
        #         print( h_value, v_value, h_cut, v_cut)
        #         max_cut = max(max_cut, v_cut * h_cut)
        #         v_last = v_value
        #         print(max_cut)
        #     h_last = h_value
        # print(max_cut)

# Solution().find_max_cake(5, 4, [1,2,4], [1,3])
# Solution().find_max_cake(5, 4, [3,1], [1])
# Solution().find_max_cake(5, 4, [3], [3])
Solution().find_max_cake(6, 7, [4,5,1], [4,5,6,3])

