
"""
Method1:

Fast pointer and slow Pointer

Method 2:

Counter and Mid Pointer and traverse pointer

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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    def find_middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        return slow.value


linked_list = LinkedList()
for i in range(1, 5):
    linked_list.add_node(i)
print(linked_list.find_middle())