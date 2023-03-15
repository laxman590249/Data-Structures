"""
Delete the least recently used from cache


Solution:

Use doubly linked list to store the keys and according to use remove or add
Use dictionary to check the element is present or not

"""


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = dict()
        self.queue = list()

    def put(self, key, value):
        if len(self.queue) == self.capacity:
            first_key = self.queue.pop(0)
            del self.map[first_key]
        self.map[key] = value
        self.queue.append(key)

    def get(self, key):
        if key not in self.map:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.map.get(key)
