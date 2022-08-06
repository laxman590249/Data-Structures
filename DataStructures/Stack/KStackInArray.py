
"""

How to efficiently implement k stacks in a single array?

"""


"""
Method 2 (A space efficient implementation) The idea is to use two extra arrays for efficient implementation of k
stacks in an array. This may not make much sense for integer stacks, but stack items can be large for example stacks
of employees, students, etc where every item is of hundreds of bytes. For such large stacks, the extra space used is
comparatively very less as we use two integer arrays as extra space. 
"""

