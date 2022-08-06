
"""
Recursive approach

"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6

head = N1


def search_key(head, key):
    if not head:
        return False
    if head.data == key:
        return True
    return search_key(head.next, key)

print(search_key(head, 8))
print(search_key(head, 6))