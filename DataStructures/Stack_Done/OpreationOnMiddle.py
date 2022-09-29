"""
How to implement a stack which will support the following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

"""

"""
1. Use duobly linked list to have three pointers, middle, start and end

2. Use one stack and one dequeue

    We will use a standard stack to store half of the elements and the other half of the elements which were added 
    recently will be present in the deque. Insert operation on myStack will add an element into the back of the deque.
    The number of elements in the deque stays 1 more or equal to that in the stack, however, whenever the number of 
    elements present in the deque exceeds the number of elements in the stack by more than 1 we pop an element from 
    the front of the deque and push it into the stack. The pop operation on myStack will remove an element from the 
    back of the deque. If after the pop operation, the size of the deque is less than the size of the stack, 
    we pop an element from the top of the stack and insert it back into the front of the deque so that size of the 
    deque is not less than the stack. We will see that the middle element is always the front element of the deque. 
    So deleting of the middle element can be done in O(1) if we just pop the element from the front of the deque.  


"""