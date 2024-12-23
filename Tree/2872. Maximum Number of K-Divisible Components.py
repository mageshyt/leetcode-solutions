"""There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.

Example 1:


Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
Output: 2
Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
- The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
It can be shown that no other valid split has more than 2 connected components.
"""


from typing import List
from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        result=0
        visited=set()

        def dfs(node):
            nonlocal result
            total=values[node]
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    total+=dfs(neighbor)

            if total%k==0:
                result+=1
                return 0

            return total

            
               
        dfs(0)

        return result

n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6

print(Solution().maxKDivisibleComponents(n, edges, values, k)) # 2


