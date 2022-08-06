"""
RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also removing a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of same values the multiset contains.

Solution:
Can be done using Dictionary and its count
"""


class RandomizedCollection:
    max_key = 0
    max_count = 0

    def __init__(self):
        self.random_set = {}

    def insert(self, val: int) -> bool:
        self.random_set[val] = self.random_set.get(val, 0) + 1
        if self.random_set[val] >= RandomizedCollection.max_count:
            RandomizedCollection.max_count = self.random_set[val]
            RandomizedCollection.max_key = val
        return self.random_set[val] == 1

    def remove(self, val: int) -> bool:
        check = self.random_set.get(val, 0)
        self.random_set[val] = self.random_set.get(val, 0) - 1
        if self.random_set[val] == -1:
            self.random_set[val] = 0
        return check > 0

    def getRandom(self) -> int:
        # max_number = 0
        # max_key = 0
        # for i, j in enumerate(self.random_set):
        #     if j > max_number:
        #         max_key = i
        #         max_number = j
        # return max_number
        return RandomizedCollection.max_key

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()