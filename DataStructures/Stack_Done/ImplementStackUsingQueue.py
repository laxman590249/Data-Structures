"""

We are given a Queue data structure that supports standard operations like enqueue() and dequeue().
We need to implement a Stack data structure using only instances of Queue and queue operations allowed on the instances.

"""

"""

Solution:

1. Use push operation heavy
    
    push(): empty q1, fill q2
    insert new element into q1
    insert from q2 to q1 

2. Use pop operation heavy

    pop(): empty q1 until 1 element is left to q2
            remove last element form q1
            insert all elements into q1 from q2

3. Use only one queue
    push(O(N))
    
    While pushing new element enqueue it 
    dequeue all elements till new element and enqueue again
    

"""