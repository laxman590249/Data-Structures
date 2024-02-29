from collections import deque
import heapq
from time import time

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru_queue = deque()
        self.priority_queue = []

    def _get_current_time(self):
        return int(time())

    def set(self, key, value, priority, expiration):
        # Add to dictionary
        self.cache[key] = (value, priority, expiration)

        # Add to priority queue based on priority and expiration
        heapq.heappush(self.priority_queue, (priority, expiration, key))

        # Append to the right of deque for LRU order
        self.lru_queue.append(key)

        # Check and evict if capacity is exceeded
        if len(self.cache) > self.capacity:
            # Find the LRU key from the left of the deque
            lru_key = self.lru_queue.popleft()
            # Remove it from the dictionary and priority queue
            del self.cache[lru_key]
            self.priority_queue = [(p, e, k) for p, e, k in self.priority_queue if k != lru_key]

    def get(self, key):
        if key in self.cache:
            # Update LRU order
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache[key][0]
        else:
            return None

    def evict_expired_items(self):
        current_time = self._get_current_time()
        while self.priority_queue and self.priority_queue[0][1] <= current_time:
            _, _, key = heapq.heappop(self.priority_queue)
            del self.cache[key]

    def evict_lowest_priority_item(self):
        if self.priority_queue:
            _, _, key = heapq.heappop(self.priority_queue)
            del self.cache[key]

    def _get_current_time(self):
        # Implement this function to get the current time
        pass

# Usage example
cache = Cache(capacity=5)
cache.set("A", 5, 5, 10001)
cache.set("B", 4, 1, 40006)
cache.set("C", 3, 5, 10001)
cache.set("D", 2, 9, 500)
cache.set("E", 1, 5, 10004)
cache.get("C")
cache.set("F", 10, 5, 5001)
cache.set("G", 9, 5, 5004)
cache.set("H", -1, 5, 5009)
cache.set("I", 1, 5, 5011)
cache.evict_expired_items()
cache.evict_lowest_priority_item()
