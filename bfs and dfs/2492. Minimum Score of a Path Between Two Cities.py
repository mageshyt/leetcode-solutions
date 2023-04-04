"""You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
 """

import collections


class Solution:
    def minScore(self, n: int, roads) -> int:

        # 1. build graph
        graph = collections.defaultdict(list)

        for u, v, w in roads:
            # (v, w) is a tuple v is the next node, w is the weight
            graph[u].append((v, w))
            # (u, w) is a tuple u is the next node, w is the weight
            graph[v].append((u, w))

        # 2. dfs

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            nonlocal min_weight

            for v, w in graph[node]:
                min_weight = min(min_weight, w)
                dfs(v)

        visited = set()
        min_weight = float('inf')
        dfs(1)

        return min_weight


if __name__ == "__main__":
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    print(Solution().minScore(n, roads))
