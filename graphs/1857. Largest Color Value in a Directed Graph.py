"""There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n"""

from collections import *


class Solution:
    def largestPathValue(self, colors: str, edges) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)

        def dfs(node):

            if node in path:
                return float('-inf')

            if node in visited:
                return 0

            path.add(node)
            visited.add(node)

            # this will give the index of the color
            colorIdx = ord(colors[node])-97

            # initially we will have one color in the path
            count_color[node][colorIdx] = 1

            for nei in adj[node]:
                if dfs(nei) == float('-inf'):
                    return float('-inf')

                for col in range(26):
                    count_color[node][col] = max(
                        count_color[node][col], count_color[nei][col] + (1 if col == colorIdx else 0))

            path.remove(node)  # remove the node from the path

            return count_color[node][colorIdx]

        path, visited = set(), set()

        res = 0

        # [node][color] = count of color in the path
        count_color = [[0]*26 for _ in range(len(colors))]

        for node in range(len(colors)):

            res = max(dfs(node), res)

        return -1 if res == float('-inf') else res


if __name__ == '__main__':
    print(Solution().largestPathValue(colors="abaca",
          edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))
    print(Solution().largestPathValue(colors="a", edges=[[0, 0]]))
