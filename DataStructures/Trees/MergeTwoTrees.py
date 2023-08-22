class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 or not node2:
                continue

            node1.val += node2.val

            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))

            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))

        return root1


# Example usage
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

solution = Solution()
merged_root = solution.mergeTrees(root1, root2)
# The merged tree should have values: 3, 4, 5, 4, 5, 7