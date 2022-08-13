

class BinHeap:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, value):
        self.size += 1
        self.heap.append(value)
        self.perc_up()

    def perc_up(self):
        current = self.size
        parent = self.size//2
        while parent > 0:
            if self.heap[current] > self.heap[parent]:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
                parent = current//2
            else:
                break

    def delete_node(self, value):
        index = self.heap.index(value)
        self.heap[index] = self.heap[self.size]
        del self.heap[self.size]
        self.size -= 1

        while index//2 > 0 and self.heap[index//2] < self.heap[index]:
            self.heap[index//2], self.heap[index] = self.heap[index], self.heap[index//2]
            index = index // 2

        while (2*index <= self.size and self.heap[index] < self.heap[2*index]) or ((2*index+1) <= self.size and self.heap[index] < self.heap[2*index+1]):
            if (2*index+1) <= self.size:
                if self.heap[2*index+1] > self.heap[2*index]:
                    self.heap[2*index+1], self.heap[index] = self.heap[index], self.heap[2*index+1]
                    index = 2*index+1
                else:
                    self.heap[2*index], self.heap[index] = self.heap[index], self.heap[2*index]
                    index = 2*index
            else:
                self.heap[2*index], self.heap[index] = self.heap[index], self.heap[2*index]
                index = 2*index

    def __str__(self):
        return str(self.heap[1:])


tree = BinHeap()
tree.insert(10)
tree.insert(20)
tree.insert(14)
tree.insert(2)
tree.insert(200)
tree.insert(100)
tree.insert(150)
tree.insert(250)
tree.insert(15)
print(tree)
tree.delete_node(200)
print(tree)





