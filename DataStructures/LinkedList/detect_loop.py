"""
Solution:

1. Hashmap  O(N) O(N)
2. Update DS and add a flag, Visited O(N) O(1)
3. Floyd’s Cycle-Finding Algorithm O(N) O(1)
4. Marking visited nodes without modifying the linked list data structure  O(N) O(1)
    In this method, a temporary node is created. The next pointer of each node that is traversed is made to point to
    this temporary node. This way we are using the next pointer of a node as a flag to indicate whether the node has
    been traversed or not. Every node is checked to see if the next is pointing to a temporary node or not. In the case
    of the first node of the loop, the second time we traverse it this condition will be true, hence we find that loop
    exists. If we come across a node that points to null then the loop doesn’t exist.
5.




"""