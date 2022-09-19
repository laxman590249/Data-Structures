"""
iven an array of size n that has the following specifications:

Each element in the array contains either a policeman or a thief.
Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than K units away from the policeman.
We need to find the maximum number of thieves that can be caught.
Examples:


Input : arr[] = {'P', 'T', 'T', 'P', 'T'},
            k = 1.
Output : 2.

Solution:

Time Complexity: O(N)
Auxiliary Space: O(1)

1. Get the lowest index of policeman p and thief t. Make an allotment
if |p-t| <= k and increment to the next p and t found.
2. Otherwise increment min(p, t) to the next p or t found.
3. Repeat above two steps until next p and t are found.
4. Return the number of allotments made.

"""