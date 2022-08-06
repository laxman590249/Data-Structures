

"""
Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, 
else false.

Method1: O(N), O(N)

    Use Stack till the half or completely


Method2 **:

    By reversing the half list
    and comparing it with the other half

Method 3 Resursive:
    








"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(2)
N5 = Node(1)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

head = N1


def find_pallindrome_stack(head):
    stack = []
    fast = head
    slow = head
    while fast and fast.next:
        stack.append(slow.data)
        fast = fast.next.next
        slow = slow.next
    if fast:
        slow = slow.next
    print(stack)
    while slow:
        if slow.data != stack.pop():
            break
        slow = slow.next
    if len(stack) == 0:
        return True
    else:
        return False

# print(find_pallindrome_stack(head))

def find_palindrom(head):
    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        next = slow.next
        slow.next = prev
        prev = slow
        slow = next

    if fast:
        slow = slow.next

    result = True
    while slow and prev:
        if slow.data != prev.data:
            result = False
            break
        slow = slow.next
        prev = prev.next

    if slow or prev:
        result = False
    return result

print(find_palindrom(head))





