"""
There are two singly linked lists in a system. By some programming error,
the end node of one of the linked list got linked to the second list,
forming an inverted Y shaped list. Write a program to get the point where two linked list merge.
"""

"""
Method 3(Using difference of node counts) 

Get count of the nodes in the first list, let count be c1.
Get count of the nodes in the second list, let count be c2.
Get the difference of counts d = abs(c1 – c2)
Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes
Then we can traverse both the lists in parallel till we come across a common node. (Note that getting a common node is done by comparing the address of the nodes)

"""

from GeeksofGeeks.linkedlist.linklist import LinkedList


def get_count(link_list):
    count = 0
    current_node = link_list.head
    while current_node:
        count += 1
        current_node = current_node.next
    return count


def find_intersection(link_1, link_2):
    count_1 = get_count(link_1)
    count_2 = get_count(link_2)
    diff = abs(count_1 - count_2)
    current_1 = link_1.head
    current_2 = link_2.head
    for i in range(diff):
        if count_1 > count_2:
            current_1 = current_1.next
        else:
            current_2 = current_2.next
    while current_2 != current_1:
        current_1 = current_1.next
        current_2 = current_2.next
    print(current_1.value)


link = LinkedList()
link_2 = LinkedList()
link.add_node(1)
link.add_node(2)
node = link.add_node(3)
link.add_node(4)
link.add_node(5)
link.add_node(6)
link_2.add_node(10)
link_2.add_node(11)
node_2 = link_2.add_node(12)
node_2.next = node
link.print_link_list()
link_2.print_link_list()
find_intersection(link, link_2)
