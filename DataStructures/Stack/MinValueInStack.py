"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

>

Solution 1:

We can store two stacks, one for elements and one for minimum value which is called Auxillary Stack

Solution 2:

Store one more element in stack with all values, min

Solution 3: (Must) O(1), O(1)

Do not store original values in the stack, do one mathematical operation on it

push(stack_value = 2 * value - min), and maintain the min

When we do pop

value = pop()

there would be two cases,

1. value < curr_min : (Update the min if popped value if less then the min)
        curr_min = 2 * curr_min - value

2. value > curr_min : do not do anything, curr_min will be same




"""