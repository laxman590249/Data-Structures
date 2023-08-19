import time


class CacheItem:
    def __init__(self, key, value, priority, expiration):
        self.key = key
        self.value = value
        self.priority = priority
        self.expiration = expiration
        self.last_access_time = time.time()
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = CacheItem(None, None, None, None)
        self.tail = CacheItem(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_end(self, item):
        last_item = self.tail.prev
        last_item.next = item
        item.prev = last_item
        item.next = self.tail
        self.tail.prev = item

    def remove(self, item):
        prev_item = item.prev
        next_item = item.next
        prev_item.next = next_item
        next_item.prev = prev_item


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_order = DoublyLinkedList()

    def _evict_expired_items(self):
        current_time = time.time()
        expired_items = [item for item in self.cache.values() if item.expiration <= current_time]
        for item in expired_items:
            self._remove_item(item)

    def _remove_item(self, item):
        self.access_order.remove(item)
        del self.cache[item.key]

    def _evict_lru_item(self):
        min_priority_item = min(self.cache.values(), key=lambda item: (item.priority, item.last_access_time))
        self._remove_item(min_priority_item)

    def Set(self, key, value, priority, expiration):
        if len(self.cache) >= self.capacity:
            self._evict_expired_items()

            if len(self.cache) >= self.capacity:
                self._evict_lru_item()

        new_item = CacheItem(key, value, priority, expiration)
        self.cache[key] = new_item
        self.access_order.add_to_end(new_item)

    def Get(self, key):
        if key in self.cache:
            item = self.cache[key]
            current_time = time.time()

            if item.expiration >= current_time:
                # Remove the item from its current position
                self.access_order.remove(item)

                # Add the item to the end of the linked list
                self.access_order.add_to_end(item)

                item.last_access_time = current_time
                return item.value
            else:
                self._remove_item(item)
                return None
        else:
            return None


current_time = 0
time.time = lambda: current_time
# Example usage
C = Cache(capacity=5)
C.Set(key="A", value=5, priority=5, expiration=10001)
C.Set(key="B", value=4, priority=1, expiration=40006)
C.Set(key="C", value=3, priority=5, expiration=10001)
C.Set(key="D", value=2, priority=9, expiration=500)
C.Set(key="E", value=1, priority=5, expiration=10004)
print(C.Get("C"))  # Output: 3

# Simulating time passing
current_time = 900
time.time = lambda: current_time

C.Set(key="F", value=10, priority=5, expiration=5001)
C.Set(key="G", value=9, priority=5, expiration=5004)
C.Set(key="H", value=-1, priority=5, expiration=5009)
C.Set(key="I", value=1, priority=5, expiration=5011)
C.Set(key="C", value=1, priority=5, expiration=5021)
print(C.Get("D"))  # Output: None
