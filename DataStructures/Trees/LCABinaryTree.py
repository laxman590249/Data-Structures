"""


Solution 1:

Root is pointing to the node with value 1, as its value doesn’t match with { 5, 6 }. We look for the key in left subtree and right subtree.

Left Subtree :
New Root = { 2 } ≠ 5 or 6, hence we will continue our recursion
New Root = { 4 } , it’s left and right subtree is null, we will return NULL for this call
New Root = { 5 } , value matches with 5 so will return the node with value 5
The function call for root with value 2 will return a value of 5
Right Subtree :
Root = { 3 } ≠ 5 or 6 hence we continue our recursion
Root = { 6 } = 5 or 6 , we will return the this node with value 6
Root = { 7 } ≠ 5 or 6, we will return NULL
So the function call for root with value 3 will return node with value 6
As both the left subtree and right subtree of the node with value 1 is not NULL, so 1 is the LCA

"""