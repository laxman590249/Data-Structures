
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


def swap_nodes(head_ref, x, y):
    head = head_ref

    # Nothing to do if x and y are same
    if (x == y):
        return None

    a = None
    b = None

    # search for x and y in the linked list
    # and store their pointer in a and b
    while (head_ref.next != None):

        if ((head_ref.next).data == x):
            a = head_ref

        elif ((head_ref.next).data == y):
            b = head_ref

        head_ref = ((head_ref).next)

    # if we have found both a and b
    # in the linked list swap current
    # pointer and next pointer of these
    if (a != None and b != None):
        temp = a.next
        a.next = b.next
        b.next = temp
        temp = a.next.next
        a.next.next = b.next.next
        b.next.next = temp

    return head

head = swap_nodes(N1, 6, 1)

# head = N1
while head:
    print(head.data)
    head = head.next




