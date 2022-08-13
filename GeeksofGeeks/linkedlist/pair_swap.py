"""
Given a singly linked list, write a function to swap elements pairwise.

Input : 1->2->3->4->5->6->NULL
Output : 2->1->4->3->6->5->N
ULL

Input : 1->2->3->4->5->NULL
Output : 2->1->4->3->5->NULL

Input : 1->NULL


Output : 1->NULL
"""

from GeeksofGeeks.linkedlist.linklist import LinkedList


def swap_pairs(linked_list):
    current_node = linked_list.head
    prev_node = None

    while current_node and current_node.next:
        temp = current_node.next
        current_node.next = current_node.next.next
        temp.next = current_node
        if prev_node:
            prev_node.next = temp
        else:
            linked_list.head = temp
        prev_node = current_node
        current_node = current_node.next


link = LinkedList()
link.add_node(1)
link.add_node(2)
link.add_node(3)
link.add_node(4)
link.add_node(5)
link.add_node(6)
link.print_link_list()
swap_pairs(link)
link.print_link_list()