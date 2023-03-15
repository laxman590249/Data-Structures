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

    def find_lca(self, node, a, b, v):
        if not node:
            return None

        if node.value == a or node.value == b:
            if v[0]:
                v[1] = True
            else:
                v[0] = True
            return node

        left_node = self.find_lca(node.left, a, b, v)
        right_node = self.find_lca(node.right, a, b, v)

        if left_node and right_node:
            return node
        return left_node if left_node else right_node


tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
v = [False, False]
node = tree.find_lca(tree.root, 6, 6, v)
if v[0] and v[1]:
    print(node.value)
else:
    print(None)