
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def get_root_node(self):
        return self.root

    def add_node(self, value):

        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            while node:
                if value > node.value:
                    if not node.right:
                        node.right = Node(value)
                        break
                    else:
                        node = node.right
                else:
                    if not node.left:
                        node.left = Node(value)
                        break
                    else:
                        node = node.left

    def _get(self, value):
        if not self.root:
            return None, None
        else:
            node = self.root
            parent = None
            while node:
                if node.value == value:
                    return node, parent
                else:
                    parent = node

                if node.value < value:
                    node = node.right
                else:
                    node = node.left

            return node, parent

    def delete_node(self, value):
        node, parent = self._get(value)
        if not node:
            print('Node is not present inthe tree.')
        else:
            if not node.left or not node.right:
                if not node.left:
                    child = node.right
                else:
                    child = node.left

                if node.value > parent.value:
                    parent.right = child
                else:
                    parent.left = child
            else:
                pre, pre_parent = BinarySearchTree._pre_processor(node)
                pre_parent.left = pre.right
                pre.right = node.right
                pre.left = node.left
                if node.value > parent.value:
                    parent.right = pre
                else:
                    parent.left = pre

    @staticmethod
    def _pre_processor(node):
        # return 10, 20
        parent = None
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def traverse(self):
        queue = []
        if not self.root:
            print('Tree is empty')
        else:
            queue.append(self.root)
            while queue:
                node = queue.pop()
                print(node.value, end=" ")
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        print()

    def get_node_level(self, value):

        def get_level(node, value, level):
            if not node:
                return 0

            if node.value == value:
                return level

            if value > node.value:
                return get_level(node.right, value, level + 1)
            else:
                return get_level(node.left, value, level + 1)

        return get_level(self.root, value, 1)

    def get_depth(self, node, depth):
        if not node:
            return depth

        left = self.get_depth(node.left, depth + 1)
        right = self.get_depth(node.right, depth + 1)

        return max(left, right)

    def insert_recursive(self, value):

        def insert(node, value):
            if value > node.value:
                if not node.right:
                    node.right = Node(value)
                else:
                    insert(node.right, value)
            else:
                if not node.left:
                    node.left = Node(value)
                else:
                    insert(node.left, value)

        if not self.root:
            self.root = Node(value)
        else:
            insert(self.root, value)

def pre_order(tree: BinarySearchTree):
    print('Pre Order :')

    def traverse(node):
        if node:
            print(node.value, end=" ")
            traverse(node.left)
            traverse(node.right)
    if tree:
        traverse(tree.get_root_node())
    print()


def post_order(tree: BinarySearchTree):
    print('Post Order :')

    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            print(node.value, end=" ")
    if tree:
        traverse(tree.get_root_node())
    print()


def in_order(tree: BinarySearchTree):
    print('In Order :')

    def traverse(node):
        if node:
            traverse(node.left)
            print(node.value, end=" ")
            traverse(node.right)

    if tree:
        traverse(tree.get_root_node())
    print()


tree = BinarySearchTree()
tree.add_node(4)
tree.add_node(2)
tree.add_node(6)
tree.add_node(1)
tree.add_node(3)
tree.add_node(5)
tree.add_node(7)

pre_order(tree)
# post_order(tree)
# in_order(tree)
tree.traverse()
