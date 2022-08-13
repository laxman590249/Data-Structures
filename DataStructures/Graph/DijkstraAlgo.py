"""

Uses to find the shorted distance from source to all other vertices.

It works well if there is not any negative vertices

> Start from the source
> Maintain the two array, Visited[], Distance[]
> Update all the distance from source to INF and source to 0 and update visited flag to T
> Keep track from other vertices as well and maintain the visited, distance array

"""