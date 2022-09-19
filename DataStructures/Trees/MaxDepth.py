
"""
104. Maximum Depth of Binary Tree


"""


def find_depth(root, depth):
	if not root:
		return depth
	left_depth = find_depth(root.left, depth+1)
	right_depth = find_depth(root.right, depth + 1)
	return max(left_depth, right_depth)


def find_depth_iter():
	if not root:
		return 0
	worklist = []
	num_node_level = 1
	levels = 0
	while worklist:
		node = worklist.pop()
		if node.left:
			worklist.append(node.left)
		if node.right:
			worklist.append(node.right)
		num_node_level -= 1
		if num_node_level == 0:
			levels += 1
			num_node_level = len(worklist)

	return levels



class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(4)
	root.right.right = Node(3)
	root.right.right.right = Node(5)
	print(find_depth(root, 0))
