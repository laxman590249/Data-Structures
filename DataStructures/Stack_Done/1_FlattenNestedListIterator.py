"""

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

"""


class NestedIterator:
    def __init__(self, nestedList: list):
        stack = [nestedList]
        self.result = []
        while stack:
            current_element = stack.pop()
            if isinstance(current_element, list):
                for element in current_element:
                    stack.append(element)
            else:
                self.result.append(current_element)

    def next(self) -> int:
        return self.result.pop()

    def hasNext(self) -> bool:
        return len(self.result)

i =NestedIterator([[1,1],2,[1,2]])
v = []
while i.hasNext():
    v.append(i.next())
print(v)