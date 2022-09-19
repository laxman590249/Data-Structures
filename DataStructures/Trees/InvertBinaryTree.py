
"""
Given the root of a binary tree, invert the tree, and return its root.

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Solution:

	Use Queue and do BFS traversal, swap left and right child of every Node.

"""


class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


def invert(root):
	queue = [root]
	while queue:
		node = queue.pop(0)
		temp = node.left
		node.left = node.right
		node.right = temp
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)

def print_tree(node):
	queue = [root]
	while queue:
		node = queue.pop(0)
		print(node.data, end='-')
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	print('')

# Driver code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	print_tree(root)
	invert(root)
	print_tree(root)

