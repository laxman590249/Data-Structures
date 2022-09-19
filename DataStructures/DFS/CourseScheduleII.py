"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.

Solution:

Directed Graph
Topology Sort

https://leetcode.com/problems/course-schedule-ii/discuss/?currentPage=1&orderBy=most_votes&query=

Topological Sort:

https://www.geeksforgeeks.org/topological-sorting/

Algo:

Create Visited List []
Create TempStack
Create DFSStack
Create TOPOStack

"""
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
visited_list = [False] * numCourses
temp_Stack = []
dfs_stack = []
topo_stack = []
graph = []
for i in range(numCourses):
    graph.append([])

for pre in prerequisites:
    graph[pre[1]].append(pre[0])

i = 0
while i < numCourses:
    if not visited_list[i]:
        dfs_stack.append(i)
        visited_list[i] = True
    while not len(dfs_stack) == 0:
        element = dfs_stack.pop()
        # print(element)
        child = graph[element]
        is_child = False
        for j in child:
            if not visited_list[j]:
                dfs_stack.append(j)
                visited_list[j] = True
                is_child = True
                print('dfs', dfs_stack)
        if not is_child:
            topo_stack.append(element)
        else:
            temp_Stack.append(element)
    print('temp', temp_Stack)
    print('dfs', dfs_stack)

    while not len(temp_Stack) == 0:
        el = temp_Stack.pop()
        topo_stack.append(el)
    i += 1

print('topo',topo_stack[::-1])






