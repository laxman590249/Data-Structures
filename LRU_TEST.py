import heapq
from time import time

class Cache:

    current_time = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_queue = []  # (priority, last_used, key)
        self.expiration_queue = [] # (expiration, key)
        self.cache = {} # (value, priority)

    def _remove_expired_item(self):
        keys_removed = []
        i = 0
        while self.expiration_queue and self.expiration_queue[i][0] < Cache.current_time:
            _, key = self.expiration_queue.pop(0)
            keys_removed.append(key)
            i += 1
        self.lru_queue = [(p, e, k) for p, e, k in self.lru_queue if k not in keys_removed]
        for key in keys_removed:
            if key in self.cache:
                del self.cache[key]

    def _remove_priority_item(self):
        _, _, key = self.lru_queue.pop(0)
        self.expiration_queue = [(expiry, key) for expiry, expiry_key in self.expiration_queue if expiry_key == key]
        del self.cache[key]

    def set(self, key, value, priority, expiration):
        self._remove_expired_item()
        if len(self.cache) > self.capacity:
            self._remove_priority_item()
        self.cache[key] = (value, priority, expiration)
        heapq.heappush(self.lru_queue, (priority, expiration, key))
        heapq.heappush(self.expiration_queue, (expiration, key))

    def get(self, key):
        self._remove_expired_item()
        if key in self.cache:
            value, priority, expiration = self.cache[key]
            self.lru_queue = [(p, e, k) for p, e, k in self.lru_queue if k == key]
            last_used = time()
            heapq.heappush(self.lru_queue, (priority, last_used, key))
            return value
        else:
            return None
    def print(self):
        print(self.cache, self.lru_queue, self.expiration_queue)

C = Cache(capacity=5)

C.set(key="A", value=5, priority=5, expiration=1000)
C.set(key="B", value=4, priority=1, expiration=4000)
C.set(key="C", value=3, priority=5, expiration=1000)
C.set(key="D", value=2, priority=9, expiration=500)
C.set(key="E", value=1, priority=5, expiration=1000)

print("Value of key 'C' after setting:", C.get("C"))  # Output: 3

Cache.current_time = 900
print("Current Time:", Cache.current_time)

C.set(key="F", value=10, priority=5, expiration=5001)  # Evicts 'D'
C.set(key="G", value=9, priority=5, expiration=5004)  # Evicts 'B'
C.set(key="H", value=-1, priority=5, expiration=5009)  # Evicts 'A'
C.set(key="I", value=1, priority=5, expiration=5011)  # Evicts 'E'
C.set(key="C", value=1, priority=5, expiration=5012)  # Overwrites 'C'
C.print()
Cache.current_time = 6000
print(Cache.current_time)
print("Value of key 'D' after eviction:", C.get("D"))  # Output: None
print("Value of key 'B' after eviction:", C.get("B"))  # Output: None
print("Value of key 'A' after eviction:", C.get("A"))  # Output: None
print("Value of key 'E' after eviction:", C.get("E"))  # Output: None
print("Value of key 'C' after overwriting:", C.get("C"))  # Output: 1