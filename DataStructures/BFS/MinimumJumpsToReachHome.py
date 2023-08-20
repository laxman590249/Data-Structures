"""
1654. Minimum Jumps to Reach Home
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i],
and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home.
If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.


"""

from collections import deque


def minJumps(forbidden, a, b, x):
    # Convert the forbidden list to a set for faster lookup
    forbidden_set = set(forbidden)

    # Initialize the queue with (position, steps, direction) tuples
    queue = deque([(0, 0, 1)])  # Starting from position 0, steps taken, direction (1 = forward)
    visited = set([(0, 1)])  # Set of (position, direction) tuples that have been visited

    while queue:
        position, steps, direction = queue.popleft()

        # Check if the bug has reached the target position
        if position == x:
            return steps

        # Try jumping forward by 'a' positions
        next_forward = position + a
        if next_forward <= x + b and next_forward not in forbidden_set and (next_forward, 1) not in visited:
            visited.add((next_forward, 1))
            queue.append((next_forward, steps + 1, 1))

        # Try jumping backward by 'b' positions if allowed
        if direction == 1 and position >= b:
            next_backward = position - b
            if next_backward not in forbidden_set and (next_backward, -1) not in visited:
                visited.add((next_backward, -1))
                queue.append((next_backward, steps + 1, -1))

    return -1
