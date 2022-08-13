class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_last(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            t_head = self.head
            while t_head.next:
                t_head = t_head.next
            t_head.next = node

    def add_first(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove_last(self):
        if not self.head:
            print("Linked list is Empty")
        elif not self.head.next:
            item = self.head
            self.head = None
            print(item.value)
        else:
            pre_node = None
            node = self.head
            while node.next:
                pre_node = node
                node = node.next
            item = node
            pre_node.next = None
            print(item.value)

    def remove(self, value):
        previous = None
        if not self.head:
            print('Item is not there in linked list')
        elif not self.head.next:
            if self.head.value == value:
                self.head = None
                print('Deleted Value:', value)
            else:
                print('Item is not there in linked list')
        else:
            node = self.head
            while node:
                if node.value == value:
                    if not previous:
                        self.head = node.next
                    else:
                        previous.next = node.next
                    break;
                previous = node
                node = node.next
            else:
                print('Item is not there in linked list')

    def reverse(self):
        node = self.head
        prev_node = None
        while node:
            next = node.next
            node.next = prev_node
            prev_node = node
            node = next
        self.head = prev_node

    def print(self):
        node = self.head
        while node:
            print(node.value, end='->')
            node = node.next
        print('END')


link = LinkedList()
link.add_last(10)
link.add_last(20)
link.add_last(30)
link.add_last(40)
link.add_first(1)
link.print()
link.reverse()
link.print()







