"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/


Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
 and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.


Solution:

1) Find inorder and preorder traversals of T, and store them in two auxiliary arrays inT[] and preT[].
2) Find inorder and preorder traversals of S, and store them in two auxiliary arrays inS[] and preS[].
3) If inS[] is a subarray of inT[] and preS[] is a subarray preT[], then S is a subtree of T. Else not.

"""