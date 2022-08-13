


class Node:

    def __init__(self, value):
        self.value = value
        self.edges = []

    def __str__(self):
        return f'Node value : {self.value}'


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, value, parent=None):
        queue = []
        if not self.root:
            self.root = Node(value)
        else:
            queue.append(self.root)
            while len(queue) > 0:
                node = queue[0]
                if node.value == parent:
                    node.edges.append(Node(value))
                    print(f'Added node under parent {parent}')
                    break
                queue = queue + node.edges
                del queue[0]
        print('Added Node into tree')

    def traverse(self):
        queue = []
        if not self.root:
            print('Tree is empty')
        else:
            queue.append(self.root)
            while len(queue) > 0:
                node = queue[0]
                print(node.value, end=" ")
                queue = queue + node.edges
                del queue[0]


tree = Tree()
tree.add_node(10)
tree.add_node(20, 10)
tree.add_node(30, 10)
tree.add_node(50, 10)
tree.add_node(15, 20)
tree.add_node(17, 20)
tree.add_node(18, 20)
tree.add_node(35, 30)
tree.add_node(56, 50)
tree.add_node(58, 50)
tree.add_node(59, 56)
tree.traverse()





