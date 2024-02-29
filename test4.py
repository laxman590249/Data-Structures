numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
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

    while dfs_stack:
        element = dfs_stack.pop()
        childs = graph[element]
        is_child = False
        for j in childs:
            if not visited_list[j]:
                dfs_stack.append(j)
                visited_list[j] = True
                is_child = True
        if is_child:
            temp_Stack.append(element)
        else:
            topo_stack.append(element)

    while temp_Stack:
        topo_stack.append(temp_Stack.pop())
    i += 1

print('topo',topo_stack[::-1])



