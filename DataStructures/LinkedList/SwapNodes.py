
"""
Swap nodes in a linked list without swapping data

Method 1: O(N), O(1)
    Naive approach (Keep track of X, Y and respective previous) with two loops

Method 2:
    Finding X, Y and there respective previous in one loop
    but find only prev_x and Prev_y there is no need to go to x, y with two other pointers

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

def swap_nodes(head, x, y):
    a_node = None
    b_node = None
    while head.next and ( not a_node or not b_node):

        if head.next.data == x:
            a_node = head
        elif head.next.data == y:
            b_node = head

        head = head.next
    temp = a_node.next.next
    a_node.next.next = b_node.next.next
    b_node.next.next = temp
    a_node.next, b_node.next = b_node.next, a_node.next

swap_nodes(N1, 1, 6)

head = N1
while head:
    print(head.data)
    head = head.next




