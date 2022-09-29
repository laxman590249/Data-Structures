"""

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)/42652


Solution:

Traverse the linked list and everytime point from old node to new node

 1 -> 2 -> 3 -> 4

 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'

 Now traverse the list again and using the random pointer, in new node point to its old random to next

 Now traverse again and separate both the linked list

"""


