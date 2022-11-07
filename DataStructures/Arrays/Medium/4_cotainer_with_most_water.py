"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Solution:

Use Two pointer approach, start from start and end
If any hight is less then other then it needs to be shifted
find the area everytime and get the max of it
"""

height = [1,8,6,2,5,4,8,3,7]
i = 0
j = len(height)-1
max_area = 0
while i < j:
    curr_height = min(height[i], height[j])
    max_area = max(max_area, curr_height * (j-i))
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
print(max_area)
