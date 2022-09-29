
class DeQueueu(object):

    def __init__(self):
        self.dequeue = []

    def add_front(self, item):
        self.dequeue.insert(0, item)

    def add_rear(self, item):
        self.dequeue.append(item)

    def remove_front(self):
        size = len(self.dequeue)
        if size == 0:
            print("Dequeue is empty")
        else:
            item = self.dequeue[0]
            del self.dequeue[0]
            return item

    def remove_rear(self):
        size = len(self.dequeue)
        if size == 0:
            print("Dequeue is empty")
        else:
            item = self.dequeue[size-1]
            del self.dequeue[size-1]
            return item

    def size(self):
        return len(self.dequeue)
