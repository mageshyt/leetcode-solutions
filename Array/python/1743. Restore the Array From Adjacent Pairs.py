
from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 1. Build a graph
        graph =defaultdict(list)

        for pair in adjacentPairs:
            x, y = pair

            graph[x].append(y)
            graph[y].append(x)


        # 2. Find the start point
        start = None

        for key in graph:
            if len(graph[key]) == 1:
                start = key
                break

        # 3. Traverse the graph
        visited = set()
        ans = []

        def dfs(node):
            visited.add(node)
            ans.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)

        return ans
    
    # Time complexity: O(N)
    # Space complexity: O(N)
