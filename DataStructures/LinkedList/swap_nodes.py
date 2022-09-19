"""
Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links.
Swapping data of nodes may be expensive in many situations when data contains many fields.

It may be assumed that all keys in the linked list are distinct.
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_link_list(self):
        current = self.head
        while current:
            print(current.value, ' -> ', end='')
            current = current.next
        print()

    def find_node(self, value):
        current = self.head
        previous = None
        if current:
            while current:
                if current.value == value:
                    break
                previous = current
                current = current.next
        return current, previous

    def swap_nodes(self, x, y):
        current_x, previous_x = self.find_node(x)
        current_y, previous_y = self.find_node(y)

        if current_y and current_x:
            if previous_x and previous_y:
                if previous_x == current_y:
                    temp = current_x.next
                    current_x.next = current_y
                    current_y.next = temp
                    previous_y.next = current_x
                elif current_x == previous_y:
                    temp = current_y.next
                    current_y.next = current_x
                    current_x.next = temp
                    previous_x.next = current_y
                else:
                    temp = current_x.next
                    previous_y.next = current_x
                    previous_x.next = current_y
                    current_x.next = current_y.next
                    current_y.next = temp
            else:
                if previous_x:
                    pass
                # Handle haed node
        else:
            print('Both Node not present')



link = LinkedList()
link.add_node(1)
link.add_node(2)
link.add_node(3)
link.add_node(4)
link.add_node(5)
link.print_link_list()
link.swap_nodes(2, 5)
link.print_link_list()


