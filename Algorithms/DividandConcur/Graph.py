'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import math


class Node:

    def __init__(self, value):
        self.value = value
        self.edge = None


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.below = None


class Tree:

    def __init__(self):
        self.start = None

    def add_tree_node(self, value):
        if not self.start:
            self.start = TreeNode(value);
        else:
            temp = self.start
            while not temp.below:
                temp = temp.below
            temp.below = TreeNode(value)

    def add_edge_in_tree(self, v1, v2):
        temp = self.start
        while temp.value != v1:
            temp = temp.below

        if not temp.right:
            temp.right = Node(v2)
        else:
            while not temp.right:
                temp = temp.right
            temp.right = Node(v2)

    def add_edge(self, v1, v2):
        self.add_edge_in_tree(v1, v2)
        self.add_edge_in_tree(v2, v1)

    def find_direction(self, v1, v2):
        temp = self.start
        distances = []
        tree_nodes = []
        index = 0

        while temp:
            distances[index] = 10
            tree_nodes[index] = temp.value
            temp = temp.below


n = int(input())
# peoples = []
tree = Tree()

for i in range(n):
    # peoples.append(int(input()))
    tree.add_tree_node(int(input()))

edges = int(input())

for i in range(edges):
    e = input().split()
    tree.add_edge(int(e[0]), int(e[1]))













