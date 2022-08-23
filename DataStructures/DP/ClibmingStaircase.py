"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

N = 1, 1
N = 2, 2
N = 3, 3
N = 4, 5

The key intuition to solve the problem is that given a number of stairs n,
if we know the number ways to get to the points [n-1] and [n-2] respectively, denoted as n1 and n2 ,
then the total ways to get to the point [n] is n1 + n2. Because from the [n-1] point,
we can take one single step to reach [n]. And from the [n-2] point, we could take two steps to get there.

It is fibonacci series

"""