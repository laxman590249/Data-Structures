"""
Build a max heap from the input data.
At this point, the maximum element is stored at the root of the heap. Replace it with the last item of the heap
followed by reducing the size of the heap by 1. Finally, heapify the root of the tree.
Repeat step 2 while the size of the heap is greater than 1.

Time Complexity: O(N log N)
Auxiliary Space: O(1)
Not Stable

"""


list_1 = [50, 60, 10, 20, 30, 40]

heap = [0]
ele = 1
sort = []


class HeapTree:

    def __init__(self):
        self.heap = [0]

    def add_ele(self, value):
        self.heap.append(value)
        self.heapify()

    def heapify(self):
        current = len(self.heap)-1
        while current > 1:
            parent = current//2
            if self.heap[parent] > self.heap[current]:
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break

    def delete_root(self):
        if len(self.heap) == 1:
            return
        else:
            ele = self.heap[1]
            self.heap[1] = self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            self.do_heap()
        return ele

    def do_heap(self):
        if len(self.heap) == 1:
            return
        else:
            current = 1
            while current < len(self.heap)-1:
                child_1 = current * 2
                child_2 = current * 2 + 1
                if child_1 > (len(self.heap)-1):
                    break
                else:
                    node = child_1
                    if child_2 <= (len(self.heap)-1):
                        if self.heap[child_1] > self.heap[child_2]:
                            node = child_2
                    self.heap[current], self.heap[node] = self.heap[node], self.heap[current]
                    current = node

    def __str__(self):
        if len(self.heap) == 1:
            return 'It is Empty'
        else:
            return str(self.heap)

    def __len__(self):
        return len(heap.heap)-1


heap = HeapTree()

for i in list_1:
    heap.add_ele(i)


def heap_sort(tree):
    if not len(tree):
        return
    node = tree.delete_root()
    sort.append(node)
    heap_sort(tree)


heap_sort(heap)

print(heap)
print(sort)










