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


"""
Solution 1:

Find the path from Root to that Node
Then find the first common node from end to Start

Solution 2:

Root is pointing to the node with value 1, as its value doesn’t match with { 5, 6 }. We look for the key in left subtree and right subtree.

Left Subtree :
New Root = { 2 } ≠ 5 or 6, hence we will continue our recursion
New Root = { 4 } , it’s left and right subtree is null, we will return NULL for this call
New Root = { 5 } , value matches with 5 so will return the node with value 5
The function call for root with value 2 will return a value of 5
Right Subtree :
Root = { 3 } ≠ 5 or 6 hence we continue our recursion
Root = { 6 } = 5 or 6 , we will return the this node with value 6
Root = { 7 } ≠ 5 or 6, we will return NULL
So the function call for root with value 3 will return node with value 6
As both the left subtree and right subtree of the node with value 1 is not NULL, so 1 is the LCA

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def side_view(self):
        queue = [self.root]
        level_length = 1
        current_count = 0
        while queue:
            current_count += 1
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if current_count == level_length:
                current_count = 0
                level_length = len(queue)
                print(node.value)

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(10)
tree.root.right.right.left.left = Node(11)
tree.root.right.right.left.left.right = Node(12)
tree.root.left.right.left = Node(10)
tree.root.left.right.left.left = Node(11)
tree.root.left.right.left.left.right = Node(12)
tree.root.left.right.left.left.right.right = Node(13)
tree.side_view()
