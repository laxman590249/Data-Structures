class Node:

    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DLL:

    def __init__(self):
        self.head = None

    def append_node(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(value)
            node.next = new
            new.prev = node

    def find_node(self, index):
        if not self.head:
            return -1
        else:
            node = self.head
            count = 0
            while node:
                if index == count:
                    return node
                node = node.next
                count += 1
            else:
                return None

    def add_node(self, value, index):
        if not self.head:
            if index > 0:
                print("Index out of bound error")
            else:
                self.head = Node(value)
        else:
            new = Node(value)
            if index == 0:
                new.next = self.head
                self.head = new
            else:
                node = self.find_node(index-1)
                if not node:
                    print("Index out of bound")
                    return
                new.next = node.next
                new.prev = node
                node.next = new

    def show(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next

    def delete(self, value):
        node = self.head
        while node:
            if value == node.value:
                break
            node = node.next
        if node:
            if not node.prev:
                self.head = node.next
            else:
                node.prev.next = node.next


link = DLL()
link.append_node(10)
link.append_node(20)
link.append_node(30)
link.append_node(40)
link.append_node(50)
link.delete(30)
link.show()
