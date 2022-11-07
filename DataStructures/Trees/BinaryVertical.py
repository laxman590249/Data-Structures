"""

           1
        /    \
       2      3
      / \   /   \
     4   5  6   7
      \         / \
       15       8  9
        \
         13


The output of print this tree vertically will be:
4
2 15
1 5 6 13
3 8
7
9

https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/


1. We can count the horizontal distance and put it in disctionary
2. Create a map with the it
3. Sort it and print it


"""