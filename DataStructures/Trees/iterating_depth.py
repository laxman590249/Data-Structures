

class NodeDepth:

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:

    def __init__(self):
        self.root = None

    def add_node(self, value, parent_value = -1, left_right="L"):
        if self.root:
            temp_node = self.root
            nodes_list = []
            while temp_node.value != parent_value:
                if temp_node.left:
                    nodes_list.append(temp_node.left)
                if temp_node.right:
                    nodes_list.append(temp_node.right)
                temp_node = nodes_list.pop()
            if left_right == 'L':
                temp_node.left = Node(value)
            else:
                temp_node.right = Node(value)
        else:
            self.root = Node(value)

    def traverse(self):
        nodes_list = []
        temp_node = self.root
        while temp_node:
            print(temp_node.value, end=' ')
            if temp_node.right:
                nodes_list.append(temp_node.right)
            if temp_node.left:
                nodes_list.append(temp_node.left)
            if nodes_list:
                temp_node = nodes_list.pop()
            else:
                break
        print()

    def find_depth(self, root, x):
        if not root:
            return -1
        dist = -1

        if root.value == x:
            return dist + 1

        dist = self.find_depth(root.left, x)
        if dist >= 0:
            return dist + 1
        dist = self.find_depth(root.right, x)
        if dist >= 0:
            return dist + 1
        return dist

    def find_parent(self, x):
        node_list = []
        temp = self.root

        while temp:
            if temp.left:
                if temp.left.value == x:
                    return temp.value
                node_list.append(temp.left)

            if temp.right:
                if temp.right.value == x:
                    return temp.value
                node_list.append(temp.right)

            temp = node_list.pop()

    def tree_height(self):
        # Base Case
        if self.root is None:
            return 0

        # Create a empty queue for level order traversal
        q = []

        # Enqueue Root and Initialize Height
        q.append(self.root)
        height = 0

        while (True):

            # nodeCount(queue size) indicates number of nodes
            # at current level
            nodeCount = len(q)
            if nodeCount == 0:
                return height

            height += 1

            # Dequeue all nodes of current level and Enqueue
            # all nodes of next level
            while (nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                nodeCount -= 1

    def tree_depth(self, x):

        if not self.root:
            return -1

        stack = [self.root]
        depth = -1

        while True:
            nodes_count = len(stack)
            if not nodes_count:
                return -1
            depth += 1
            while nodes_count:
                node = stack.pop(0)
                if node.value == x:
                    return depth
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                nodes_count -= 1

    def find_cousin(self, x, y):
        depth_x = self.find_depth(self.root, x)
        depth_y = self.find_depth(self.root, y)

        if depth_x != depth_y:
            print('Different Depth')
            return False
        else:
            parent_x = self.find_parent(x)
            parent_y = self.find_parent(y)
            if parent_x != parent_y:
                return True
            else:
                print('Same Parent')
                return False


tree = BinaryTree()
tree.add_node(1)
tree.add_node(2, 1, 'L')
tree.add_node(4, 2, 'R')
tree.add_node(3, 1, 'R')
tree.add_node(5, 3, 'R')
tree.add_node(6, 5, 'R')
tree.traverse()
print(tree.find_cousin(3, 5))
print(tree.tree_height())
print(tree.tree_depth(6))



