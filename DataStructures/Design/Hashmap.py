class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, initial_size=16, load_factor=0.75):
        self.size = initial_size
        self.load_factor = load_factor
        self.bucket_array = [None] * self.size
        self.num_elements = 0

    def _hash_function(self, key):
        return hash(key) % self.size

    def _resize(self):
        new_size = self.size * 2
        new_bucket_array = [None] * new_size

        for node in self.bucket_array:
            current = node
            while current:
                hash_value = self._hash_function(current.key, new_size)
                if new_bucket_array[hash_value] is None:
                    new_bucket_array[hash_value] = HashNode(current.key, current.value)
                else:
                    new_node = HashNode(current.key, current.value)
                    new_node.next = new_bucket_array[hash_value]
                    new_bucket_array[hash_value] = new_node
                current = current.next

        self.size = new_size
        self.bucket_array = new_bucket_array

    def put(self, key, value):
        if (self.num_elements / self.size) >= self.load_factor:
            self._resize()

        hash_value = self._hash_function(key)
        if self.bucket_array[hash_value] is None:
            self.bucket_array[hash_value] = HashNode(key, value)
        else:
            current = self.bucket_array[hash_value]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = HashNode(key, value)
        self.num_elements += 1

    def get(self, key):
        hash_value = self._hash_function(key)
        current = self.bucket_array[hash_value]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        hash_value = self._hash_function(key)
        current = self.bucket_array[hash_value]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.bucket_array[hash_value] = current.next
                self.num_elements -= 1
                return
            prev = current
            current = current.next

    def contains_key(self, key):
        hash_value = self._hash_function(key)
        current = self.bucket_array[hash_value]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def size(self):
        return self.num_elements

# Creating an instance of HashMap
my_hashmap = HashMap()

# Adding key-value pairs
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "New York")

# Getting values
print(my_hashmap.get("name"))  # Output: John
print(my_hashmap.get("age"))   # Output: 25

# Removing a key-value pair
my_hashmap.remove("age")

# Getting a non-existing value
print(my_hashmap.get("country"))  # Output: None
