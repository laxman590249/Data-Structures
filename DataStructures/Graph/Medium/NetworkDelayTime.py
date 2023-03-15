"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

"""

import collections
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: list, n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # Since the graph is directed, so we only need to append one directional
        for u, v, time in times:
            graph[u].append([v, time])

        time_needed = [float('inf')] * n
        time_needed[k - 1] = 0
        heap = [[0, k]]  # initial stage

        visited = set()  # used to record all visited nodes
        visited.add(k)

        while heap:
            time, cur_node = heappop(heap)
            print(time, cur_node)
            for nei, nei_time in graph[cur_node]:
                total_time = time + nei_time
                if total_time < time_needed[nei - 1]:
                    # No need to do additional check since it might lead to miss the optimal solution.
                    # Refer to example above. After traversing node 1's neighbor 2 and 3, the total time to node3 is 4. If we added this check, then later on, when we traverse to node2, it's neighbor also contains node3, but the time is more optimal which is 1 + 2 (3) is less than 4,
                    # so if we added this check, then we will miss the optimal solution.
                    # if nei not in visited:
                    time_needed[nei - 1] = total_time
                    visited.add(nei)
                    heappush(heap, [total_time, nei])

        return max(time_needed) if len(visited) == n else -1

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))