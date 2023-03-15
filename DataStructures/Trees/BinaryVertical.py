"""

           1
        /    \
       2      3
      / \   /   \
     4   5  6   7
      \         / \
       15       8  9
        \
         13


The output of print this tree vertically will be:
4
2 15
1 5 6 13
3 8
7
9

https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/


1. We can count the horizontal distance and put it in disctionary
2. Create a map with the it
3. Sort it and print it


"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def veritical_view(self):
        queue = [(self.root, 0)]
        level_length = 1
        current_count = 0
        positions = {}
        while queue:
            current_count += 1
            node, position = queue.pop(0)
            result = positions.get(position, [])
            result.append(node.value)
            positions[position] = result
            if node.left:
                queue.append((node.left, position-1))
            if node.right:
                queue.append((node.right, position+1))
            if current_count == level_length:
                current_count = 0
                level_length = len(queue)
        for keys in sorted(positions.keys()):
            print(','.join([str(val) for val in positions[keys]]))


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
tree.veritical_view()
