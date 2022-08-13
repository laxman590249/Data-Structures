

class Side:

    LEFT = 0
    RIGHT = 1


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, value, parent_value, side_value):

        if not self.root:
            self.root = Node(value)
        else:
            temp = self.root
            stack =[temp]

            while stack:
                temp = stack.pop()
                if temp.value == parent_value:
                    break
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)

            if side_value == Side.LEFT:
                temp.left = Node(value)
            else:
                temp.right = Node(value)

    def traverse(self):
        if not self.root:
            print('Tree is Empty')
        else:
            temp = self.root
            stack = [temp]
            while stack:
                temp = stack.pop(0)
                if temp.left:
                    stack.append(temp.left)

                if temp.right:
                    stack.append(temp.right)

                print(temp.value, end=' -> ')

    def find_height(self):
        print()

        if not self.root:
            return -1
        else:
            temp = self.root
            stack = [temp]
            height = -1

            while(True):
                count = len(stack)
                i = 1
                while count >= i:
                    temp = stack.pop(0)
                    if temp.left:
                        stack.append(temp.left)
                    if temp.right:
                        stack.append(temp.right)
                    i += 1
                height += 1
                if not stack:
                    break
            return height

    def find_height_node(self, value):
        total_height = self.find_height()
        print('Total Height', total_height)

        if not self.root:
            return -1
        else:
            temp = self.root
            stack = [temp]
            height = -1

            while(True):
                count = len(stack)
                i = 1
                height += 1
                # print(height)
                while count >= i:
                    temp = stack.pop(0)
                    if temp.value == value:
                        print('Height', height)
                        return total_height - height

                    if temp.left:
                        # print('Left', temp.value, count, i)
                        stack.append(temp.left)

                    if temp.right:
                        # print('Right', temp.value, count, i)
                        stack.append(temp.right)
                    i += 1
                if not stack:
                    print('Empty')
                    break
            # print('Height', height)
            return total_height - height


tree = Tree()
tree.add_node(1, None, None)
tree.add_node(2, 1, Side.LEFT)
tree.add_node(3, 1, Side.RIGHT)
tree.add_node(4, 2, Side.LEFT)
tree.add_node(5, 2, Side.RIGHT)
tree.add_node(6, 3, Side.LEFT)
tree.add_node(7, 3, Side.RIGHT)
tree.add_node(8, 5, Side.LEFT)
tree.traverse()
# print(tree.find_height())
print(tree.find_height_node(8))
