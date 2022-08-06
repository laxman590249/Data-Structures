
"""
Write a removeDuplicates() function that takes a list and deletes any duplicate nodes from the list.
The list is not sorted.
For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to
12->11->21->41->43.


Method 1: Two loops O(n^2), O(1)

Method 2: O(nLogn),  O(1)

    User sort, for linked list it is merge sort for efficiently sorting it

Method 3: O(N), O(N)

    Use Hashing
    We traverse the link list from head to end. For every newly encountered element, we check whether it is in the hash
    table: if yes, we remove it; otherwise we put it in the hash table.

"""