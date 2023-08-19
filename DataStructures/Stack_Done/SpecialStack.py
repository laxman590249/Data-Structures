"""
Question: Design a Data Structure SpecialStack that supports all the stack operations like
push(), pop(), isEmpty(), isFull()
and an additional operation getMin() which should return minimum element from the SpecialStack.
All these operations of SpecialStack must be O(1). To implement SpecialStack,
you should only use standard Stack data structure and no other data structure like arrays, list, . etc.

"""


"""
Approach 1:

(https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/)

1. Two stacks can be used, Main, Auxiliary 

    if min is equal to number or less then that update auxilary stack as well
     S1  S2
     
    (3)  
    (2)  
    (5)  (2)
    (3)  (3)
    (3)  (3)

2. Maintain the minimum with the main stack as we second element as minimum in a tuple
    
    (5, 2)
    (2, 2) 
    (4, 3)
    (3, 3) 
    
"""

"""
Best Approach

https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/


n approach that uses O(1) time and O(n) extra space is discussed here.
In this article, a new approach is discussed that supports minimum with O(1) extra space. We define a variable minEle 
that stores the current minimum element in the stack. Now the interesting part is, how to handle the case when minimum 
element is removed. To handle this, we push “2x – minEle” into the stack instead of x so that the previous minimum 
element can be retrieved using the current minEle and its value stored in the stack. Below are detailed steps and an 
explanation of work.

Push(x) : Inserts x at the top of stack. 

If the stack is empty, insert x into the stack and make minEle equal to x.
If the stack is not empty, compare x with minEle. Two cases arise:
If x is greater than or equal to minEle, simply insert x.
If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x. For example, let previous 
minEle was 3. Now we want to insert 2. We update minEle as 2 and insert 2*2 – 3 = 1 into the stack.


Pop() : Removes an element from top of stack. 

Remove element from top. Let the removed element be y. Two cases arise:
If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
If y is less than minEle, the minimum element now becomes (2*minEle – y), so update (minEle = 2*minEle – y). 
This is where we retrieve previous minimum from current minimum and its value in stack. For example, let the element to 
be removed be 1 and minEle be 2. We remove 1 and update minEle as 2*2 – 1 = 3.


"""


class Stack:

    def __init__(self):
        self.stack = []
        self.min_el = None
        self.length = 0

    def push(self, number):
        if not self.length:
            self.stack.append(number)
            self.min_el = number
        else:
            if self.min_el > number:
                self.stack.append(2*number - self.min_el)
                self.min_el = number
            else:
                self.stack.append(number)
        self.length += 1

    def pop(self):
        if not self.length:
            raise Exception('Stack is Empty')
        else:
            number = self.stack.pop()
            if self.min_el > number:
                self.min_el = 2 * self.min_el - number
                number = (number + self.min_el)//2
            return number

    def get_min(self):
        return self.min_el


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(5)
stack.push(-1)
stack.push(50)
print(stack.stack)
print('pop', stack.pop())
print('Min',stack.get_min())
print('pop', stack.pop())
print('Min',stack.get_min())
print('pop', stack.pop())
print('Min',stack.get_min())
print(stack.stack)



