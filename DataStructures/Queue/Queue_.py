
class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        size = len(self.queue)
        if size == 0:
            print('Queue is empty')
        else:
            item = self.queue[0]
            del self.queue[0]
            return item

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
print(queue.size())
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())