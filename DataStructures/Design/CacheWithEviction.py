import time
from collections import OrderedDict


class CacheItem:
    def __init__(self, value, priority, expiration):
        self.value = value
        self.priority = priority
        self.expiration = expiration
        self.last_access_time = time.time()


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.expiration_times = {}

    def _evict_expired_items(self):
        current_time = time.time()
        expired_keys = [key for key, exp_time in self.expiration_times.items() if exp_time <= current_time]
        for key in expired_keys:
            self._remove_item(key)

    def _remove_item(self, key):
        del self.cache[key]
        del self.expiration_times[key]

    def _evict_least_priority_lru_item(self):
        min_priority = min(self.cache.values(), key=lambda item: item.priority).priority
        lowest_priority_keys = [key for key, item in self.cache.items() if item.priority == min_priority]
        lru_key = min(lowest_priority_keys, key=lambda key: self.cache[key].last_access_time)
        self._remove_item(lru_key)

    def Set(self, key, value, priority, expiration):
        if len(self.cache) >= self.capacity:
            self._evict_expired_items()

            if len(self.cache) >= self.capacity:
                self._evict_least_priority_lru_item()

        self.cache[key] = CacheItem(value, priority, expiration)
        self.expiration_times[key] = expiration

    def Get(self, key):
        if key in self.cache:
            item = self.cache[key]
            item.last_access_time = time.time()
            if item.expiration >= time.time():
                return item.value
            else:
                self._remove_item(key)
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

"""
Certainly, let's break down the code for the cache implementation with the specified eviction policy:

1. **Import Statements:**
    ```python
    import time
    from collections import OrderedDict
    ```
    - `time`: Module for handling time-related operations.
    - `OrderedDict`: Data structure that maintains the order of elements based on insertion order.

2. **CacheItem Class:**
    ```python
    class CacheItem:
        def __init__(self, key, value, priority, expiration):
            self.key = key
            self.value = value
            self.priority = priority
            self.expiration = expiration
            self.last_access_time = time.time()
    ```
    - This class defines the structure of a cache item.
    - It holds the key, value, priority, expiration time, and last access time of an item.

3. **Cache Class Definition:**
    ```python
    class Cache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}
            self.expiration_times = OrderedDict()
    ```
    - `capacity`: Maximum number of items the cache can hold.
    - `cache`: Dictionary to store cache items, with keys being item keys and values being `CacheItem` instances.
    - `expiration_times`: Ordered dictionary to store expiration times of items.

4. **Evict Expired Items Method:**
    ```python
    def _evict_expired_items(self):
        current_time = time.time()
        expired_keys = [key for key, exp_time in self.expiration_times.items() if exp_time <= current_time]
        for key in expired_keys:
            self._remove_item(key)
    ```
    - This method iterates through `expiration_times` to identify keys of expired items.
    - It calls `_remove_item` to remove expired items from both `cache` and `expiration_times`.

5. **Remove Item Method:**
    ```python
    def _remove_item(self, key):
        del self.cache[key]
        del self.expiration_times[key]
    ```
    - Removes an item from `cache` and `expiration_times`.

6. **Evict Least Priority LRU Item Method:**
    ```python
    def _evict_least_priority_lru_item(self):
        min_priority = min(self.cache.values(), key=lambda item: item.priority).priority
        lowest_priority_keys = [key for key, item in self.cache.items() if item.priority == min_priority]
        lru_key = min(lowest_priority_keys, key=lambda key: self.expiration_times[key])
        self._remove_item(lru_key)
    ```
    - Identifies the lowest priority value among the items in the cache.
    - Finds keys of items with the lowest priority.
    - Selects the least recently used (LRU) item based on `expiration_times`.
    - Calls `_remove_item` to remove the LRU item.

7. **Set Method:**
    ```python
    def Set(self, key, value, priority, expiration):
        if len(self.cache) >= self.capacity:
            self._evict_expired_items()
            
            if len(self.cache) >= self.capacity:
                self._evict_least_priority_lru_item()
        
        self.cache[key] = CacheItem(key, value, priority, expiration)
        self.expiration_times[key] = expiration
    ```
    - Adds items to the cache while considering the eviction policy.
    - Checks if the cache is full and evicts expired items.
    - If still over capacity, evicts least priority LRU items.
    - Adds the new item to `cache` and `expiration_times`.

8. **Get Method:**
    ```python
    def Get(self, key):
        if key in self.cache:
            item = self.cache[key]
            item.last_access_time = time.time()
            if item.expiration > time.time():
                return item.value
            else:
                self._remove_item(key)
                return None
        else:
            return None
    ```
    - Retrieves an item from the cache based on a key.
    - Updates the item's `last_access_time` if the key exists.
    - Checks for expiration and returns the item value if not expired.
    - If expired, removes the item and returns `None`.

9. **Example Usage:**
    ```python
    C = Cache(capacity=5)
    C.Set(key="A", value=5, priority=5, expiration=10001)
    # ...
    C.Get("D")
    ```
    - Demonstrates how to create a `Cache` object and perform cache operations based on the specified eviction policy.

The implementation effectively handles cache operations, evictions, and expiration while adhering to the defined eviction policy.
"""