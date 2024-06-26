"""There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
"""
from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [0] * n
        ans = [0] * n

        graph = defaultdict(set)
        for src, dist in edges:
            graph[src].add(dist)
            graph[dist].add(src)

        def dfs(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

            count[node] += 1

        def dfs2(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + n - count[child]
                dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)

        return ans


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    print(Solution().sumOfDistancesInTree(n, edges))  # [8,12,6,10,10,10]
