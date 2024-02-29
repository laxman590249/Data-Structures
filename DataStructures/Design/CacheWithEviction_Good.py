"""
implement the cache with dict -=> {key: (value, exp)}
to have the expiration implement the heapq, with (exp, key)
to have the LRU, implement the DLL, ()

"""

import time
import heapq

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-value pairs
        self.lru_queue = []  # List to maintain LRU order
        self.expiration_queue = []  # Priority queue for prioritizing items by priority and expiration

    def _get_current_time(self):
        return int(time.time())

    def _evict_expired_items(self):
        current_time = self._get_current_time()
        while self.expiration_queue and self.expiration_queue[0][0] <= current_time:
            _, key = heapq.heappop(self.expiration_queue)
            del self.cache[key]

    def _evict_lru_item(self):
        _, key = self.lru_queue.pop(0)
        del self.cache[key]

    def set(self, key, value, priority, expiration):
        self._evict_expired_items()

        if len(self.cache) >= self.capacity:
            self._evict_lru_item()

        self.cache[key] = (value, expiration)
        heapq.heappush(self.expiration_queue, (expiration, key))
        self.lru_queue.append((priority, key))

    def get(self, key):
        self._evict_expired_items()

        if key in self.cache:
            value, _ = self.cache[key]
            # Update LRU queue
            self.lru_queue = [(p, k) for p, k in self.lru_queue if k != key]
            self.lru_queue.append((self._get_current_time(), key))
            return value
        else:
            return None

# Example usage
if __name__ == "__main__":
    C = Cache(capacity=5)

    C.set(key="A", value=5, priority=5, expiration=10001)
    C.set(key="B", value=4, priority=1, expiration=40006)
    C.set(key="C", value=3, priority=5, expiration=10001)
    C.set(key="D", value=2, priority=9, expiration=500)
    C.set(key="E", value=1, priority=5, expiration=10004)

    print("Value of key 'C' after setting:", C.get("C"))  # Output: 3

    current_time = 900
    print("Current Time:", current_time)

    C.set(key="F", value=10, priority=5, expiration=5001)  # Evicts 'D'
    C.set(key="G", value=9, priority=5, expiration=5004)  # Evicts 'B'
    C.set(key="H", value=-1, priority=5, expiration=5009)  # Evicts 'A'
    C.set(key="I", value=1, priority=5, expiration=5011)  # Evicts 'E'
    C.set(key="C", value=1, priority=5, expiration=5012)  # Overwrites 'C'

    print("Value of key 'D' after eviction:", C.get("D"))  # Output: None
    print("Value of key 'B' after eviction:", C.get("B"))  # Output: None
    print("Value of key 'A' after eviction:", C.get("A"))  # Output: None
    print("Value of key 'E' after eviction:", C.get("E"))  # Output: None
    print("Value of key 'C' after overwriting:", C.get("C"))  # Output: 1
