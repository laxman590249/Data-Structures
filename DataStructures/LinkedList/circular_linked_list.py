

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class CLL:

    def __init__(self):
        self.head = None

    def insert_end(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
        else:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = Node(value)
            node.next.next = self.head

    def traverse(self):
        node = self.head
        while node and node.next != self.head:
            print(node.value, end=" ")
            node = node.next
        print(node.value, end=" ")

    def get_last(self):
        if not self.head:
            return None
        else:
            node = self.head
            while self.head != node.next:
                node = node.next
            return node
        
    def insert_start(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
        else:
            last_node = self.get_last()
            node = Node(value)
            last_node.next = node
            node.next = self.head
            self.head = node

    def find_node(self, index):
        if index == -1:
            return -1
        count = 0
        node = self.head
        while node.next != self.head:
            if count == index:
                break
            node = node.next
            count += 1
        if count == index:
            return node
        else:
            return None

    def insert(self, value, index):
        if not self.head:
            if index > 0:
                print('Index out of bound.')
            else:
                node = Node(value)
                node.next = node
                self.head = node
        else:
            node = self.find_node(index-1)
            if not node:
                print('Index out of bound. S')
            else:
                new = Node(value)
                if index == 0:
                    last = self.get_last()
                    new.next = self.head
                    self.head = new
                    last.next = new
                else:
                    new.next = node.next
                    node.next = new


cll = CLL()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_end(40)
cll.insert_start(5)
cll.insert_start(2)
cll.insert(1, 0)
cll.insert(100, 1)
cll.traverse()


