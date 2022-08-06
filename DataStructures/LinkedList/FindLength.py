"""
Write a function to count the number of nodes in a given singly linked list.

1. Iterative

2. Recursive

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


def find_length(head, count=0):
    if not head:
        return count
    return find_length(head.next, count + 1)



def find_length_2(head):
    if not head:
        return 0
    return 1 + find_length(head.next)


print(find_length(head))
print(find_length_2(head))



