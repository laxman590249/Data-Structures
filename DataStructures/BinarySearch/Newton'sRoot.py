"""
Given an integer N and a tolerance level L, the task is to find the square root of that number using Newton’s Method.

Input: N = 16, L = 0.0001
Output: 4
42 = 16
Input: N = 327, L = 0.00001
Output: 18.0831

Solution:

root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.


Assign X to the N itself.
Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue.
If the calculated root comes inside the tolerance allowed then break out of the loop.
Print the root.


"""
def squareRoot(n, l) :

	x = n
	count = 0

	while (1) :
		count += 1
		root = 0.5 * (x + (n / x))
		if (abs(root - x) < l) :
			break
		x = root

	return root

# Driver code
if __name__ == "__main__" :

	n = 16
	l = 0.000000000001

	print(squareRoot(n, l))

# This code is contributed by AnkitRai01
