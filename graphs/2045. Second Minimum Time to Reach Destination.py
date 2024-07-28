
from collections import defaultdict ,deque

from typing import List
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # adj graph
        graph = defaultdict(list) # node: [neighbours]
        visited_count = defaultdict(list) # node: [visited]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        pq = deque([1])
        curr_time = 0
        res=-1

        while pq:
            for _ in range(len(pq)):
                node = pq.popleft()
                # if node is destination
                if node == n:
                    # if res is set return the minimum of res and curr_time
                    if res !=-1:
                        return curr_time
                    res = curr_time
                for nei in graph[node]:
                    curr_visited = visited_count[nei]
                    if len(curr_visited) == 0 or (len(curr_visited) == 1 and curr_visited[0] != curr_time):
                        pq.append(nei)
                        visited_count[nei].append(curr_time)

            if (curr_time// change) % 2 == 1:
                curr_time += change - (curr_time % change)
            curr_time += time


        return curr_time

# Time complexity: O(N+E)
# Space complexity

print(Solution().secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5)) # 13


