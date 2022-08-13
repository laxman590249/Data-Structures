import ctypes

class DynamicArray:

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.capacity

    def __getitem__(self, k):

        if not 0 <= k <= self.n:
            return IndexError('K is out of bound')

        return self.A[k]

    def __setitem__(self, key, value):
        if not 0 <= key <= self.capacity:
            return IndexError('K is out of bound')
        self.A[key] = value

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, newcap):

        B = self.make_array(newcap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = newcap

    def make_array(self, newcap):
        return (newcap * ctypes.py_object)()

    def __str__(self):
        result = ''
        if len(self.A)> 0:
            for i in range(len(self.A)):
                result += str(self.A[i]) + " "
        else:
            result = "Array is Empty"
        return result


arr = DynamicArray()
arr.append(1)
arr.append(1)
arr.append(3)
arr.append(4)
arr[2] = 10
print(len(arr))
print(arr[2])
print(arr)













