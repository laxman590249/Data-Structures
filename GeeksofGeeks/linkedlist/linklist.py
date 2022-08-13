from GeeksofGeeks.linkedlist.node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        return node

    def print_link_list(self):
        current = self.head
        while current:
            print(current.value, ' -> ', end='')
            current = current.next
        print()