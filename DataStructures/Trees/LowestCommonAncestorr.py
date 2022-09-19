"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

p = 0
q = 5
answer = 2

Solution:
    if root > p , root > q, root = root.left
    if root < p, root < q, root = root.right
    else return root

"""

def lowestCommonAncestor(root, p, q):
    while root:
        if p < root.data > q:
            root = root.left
        elif p > root.data < q:
            root = root.right
        else:
            return root.data

class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


if __name__ == '__main__':
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)
    root.right.left = Node(7)
    root.right.right = Node(9)
    print(lowestCommonAncestor(root, 0, 5))
