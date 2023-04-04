"""You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14."""

import collections


class Solution:
    def countPairs(self, n: int, edges) -> int:
        graph = {node: [] for node in range(n)}
        res = 0

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        reached_nodes = collections.defaultdict(list)

        def dfs(node, nodes) -> list:
            visited.add(node)
            nodes.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, nodes)

        for node in range(n):
            if node not in visited:
                dfs(node, reached_nodes[node])

        # now we found the nodes group

        for group in reached_nodes.values():
            res += len(group) * (n - len(group))

        return res // 2


if __name__ == '__main__':
    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    print(Solution().countPairs(n, edges))
