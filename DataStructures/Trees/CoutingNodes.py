''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def get_root_node(self):
        return self.root

    def find_node(self, parent):
        if self.root.value == parent:
            return self.root
        else:
            queue_list = list()
            queue_list.append(self.root)
            node = self.root
            while node.value != parent:
                node = queue_list.pop()
                if node.left:
                    queue_list.append(node.left)
                if node.right:
                    queue_list.append(node.right)
            return node

    def add_node(self, parent, child):
        if not self.root:
            node = Node(parent)
            node.left = Node(child)
            self.root = node
        else:
            node = self.find_node(parent)
            if not node.left:
                node.left = Node(child)
            else:
                node.right = Node(child)

    def get_depth(self, node, depth):
        if not node:
            return depth
        left = self.get_depth(node.left, depth + 1)
        right = self.get_depth(node.right, depth + 1)
        return max(left, right)

    def depth_all_tech(self):
        queue = []
        if not self.root:
            print(1)
        else:
            queue.append(self.root)
            while queue:
                node = queue.pop()
                print(self.find_nodes(node), end=' ')
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        print()

    def get_node_level(self, root, value):
        def get_level(node, value, level):
            if not node:
                return 0
            if node.value == value:
                return level
            d_level = get_level(node.left, value, level + 1)
            if d_level:
                return d_level
            d_level = get_level(node.right, value, level + 1)
            return d_level

        return get_level(root, value, 1)

    def find_nodes(self, base):
        node_count = 0
        if base.right:
            node = base.right
            depth = self.get_depth(node, 0)
            # print(f'Depth : {depth}, Node: {node.value}')
            queue = list()
            queue.append(node)
            while queue:
                node = queue.pop()
                level = self.get_node_level(base, node.value)
                # print(f'Level: {level}, node: {node.value}')
                if level == depth+1:
                    node_count += 1
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        if base.left:
            node = base.left
            depth = self.get_depth(node, 0)
            queue = list()
            queue.append(node)
            while queue:
                node = queue.pop()
                level = self.get_node_level(base, node.value)
                if level == depth+1:
                    node_count += 1
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        if node_count:
            return node_count
        else:
            return 1


def main():
    tree = BinaryTree()
    nodes = int(input())
    if nodes < 1:
        print(0)
    else:
        for i in range(nodes - 1):
            line = input().split(' ')
            parent = int(line[0])
            child = int(line[1])
            tree.add_node(parent, child)
        tree.depth_all_tech()

main()

