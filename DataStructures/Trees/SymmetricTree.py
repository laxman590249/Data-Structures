
"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Solution:

	Use a Stack,
	Put Root node in the stack first
	Not pop the root and put left and right node

	now iterate thorugh >
		left <- pop
		right <- pop

		check whether both values are same or not
		push left.left, push right.right
		push left.right, push right.left

	If in the end Stack is empty then its True

"""


def find_symmetric(root):
	# Write your code
	if not root:
		return False
	stack = [root.left, root.right]
	while stack:
		right = stack.pop()
		left = stack.pop()

		if left.data != right.data:
			return False

		if left.left:
			if right.right:
				stack.append(left.left)
				stack.append(right.right)
			else:
				return False
		else:
			if right.right:
				return False

		if left.right:
			if right.left:
				stack.append(left.right)
				stack.append(right.left)
			else:
				return False
		else:
			if right.left:
				return False
	return True


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
	print(find_symmetric(root))
