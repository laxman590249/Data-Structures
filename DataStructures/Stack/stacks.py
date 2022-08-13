

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        size = len(self.stack)
        if size == 0:
            print('Stack is Empty')
        else:
            item = self.stack[size-1]
            del self.stack[size-1]
            return item

    def peek(self):
        size = len(self.stack)
        if size == 0:
            print('Stack is Empty')
        else:
            item = self.stack[size-1]
            return item

    def size(self):
        return len(self.stack)



stack = Stack()
print(stack.size())
stack.push(10)
print(stack.peek())
stack.push(20)
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())