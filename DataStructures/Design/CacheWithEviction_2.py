import time
import heapq


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Linked Hash Map: key -> (value, expiration_time, priority, prev, next)
        self.expiry_heap = []  # Min-Heap for expiration and priority
        self.head = None
        self.tail = None

    def _evict(self):
        while self.expiry_heap:
            expiration_time, _, key = heapq.heappop(self.expiry_heap)
            if key in self.cache and self.cache[key][1] == expiration_time:
                self._remove_from_cache(key)
                break

    def _remove_from_cache(self, key):
        value, _, _, prev, next_node = self.cache[key]
        del self.cache[key]
        if prev:
            self.cache[prev][3] = next_node
        else:
            self.head = next_node
        if next_node:
            self.cache[next_node][4] = prev
        else:
            self.tail = prev

    def _add_to_cache(self, key, value, expiration_time, priority):
        self._evict_if_needed()
        new_node = [value, expiration_time, priority, None, self.head]
        self.cache[key] = new_node
        if self.head:
            self.cache[self.head][3] = key
        else:
            self.tail = key
        self.head = key
        heapq.heappush(self.expiry_heap, (expiration_time, priority, key))

    def _evict_if_needed(self):
        while len(self.cache) >= self.capacity:
            self._evict()

    def get(self, key):
        if key in self.cache:
            value, expiration_time, priority, prev, _ = self.cache[key]
            if expiration_time >= time.time():
                self._move_to_front(key)
                return value
            else:
                self._evict()
                return None
        return None

    def _move_to_front(self, key):
        if key != self.head:
            _, _, _, prev, next_node = self.cache[key]
            if prev:
                self.cache[prev][4] = next_node
            else:
                self.tail = next_node
            if next_node:
                self.cache[next_node][3] = prev
            else:
                return
            self.cache[key][3] = None
            self.cache[key][4] = self.head
            self.cache[self.head][3] = key
            self.head = key

    def put(self, key, value, priority, expiry_seconds):
        expiration_time = time.time() + expiry_seconds
        if key in self.cache:
            self._remove_from_cache(key)
            heapq.heappop(self.expiry_heap)

        self._add_to_cache(key, value, expiration_time, priority)

        # Remove expired entries in batches
        current_time = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] < current_time:
            _, _, expired_key = heapq.heappop(self.expiry_heap)
            if expired_key in self.cache:
                self._remove_from_cache(expired_key)

            if not self.expiry_heap:
                break

    def print_cache(self):
        node = self.head
        while node:
            key = node
            value, expiration, priority, _, next_node = self.cache[key]
            print(f"Key: {key}, Value: {value}, Expiration: {expiration}, Priority: {priority}")
            node = next_node


# Example usage
cache = LRUCache(capacity=3)
cache.put("key1", "value1", priority=2, expiry_seconds=5)
cache.put("key2", "value2", priority=1, expiry_seconds=10)
cache.put("key3", "value3", priority=3, expiry_seconds=8)
cache.print_cache()

print(cache.get("key2"))

cache.put("key4", "value4", priority=2, expiry_seconds=6)
cache.print_cache()
