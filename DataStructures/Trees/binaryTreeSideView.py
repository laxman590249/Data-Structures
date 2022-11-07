"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
 you can see ordered from top to bottom.


           1
        /    \
       2      3
      / \   /   \
     4   5  6   7
      \         / \
       15       8  9
        \
         13

Output: 1 3 7 9 13

Do a level order traversal and for every level append the last Node
"""