"""
The problem is opposite of this post. We are given a stack data structure with push and pop operations,
the task is to implement a queue using instances of stack data structure and operations on them.

"""
"""

Solution:

1> Implement it with two stacks, when do the first dequeue operation empty first stack into second and do 
dequeue from the second stack until it is empty

2> 

Recursive dequeue can be used

s = []

enqueue:

    s.append(x)

"""

s = []
def dequeue():
    
    if len(s) <= 0:
        return None
    x = s.pop()
    if len(s) <= 0:
        return x
    item = dequeue()
    s.append(x)
    return item
