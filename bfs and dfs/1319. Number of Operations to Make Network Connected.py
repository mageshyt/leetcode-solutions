"""There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables."""

import collections


class Solution:
    def makeConnected(self, n: int, connections) -> int:

        if len(connections) < n - 1:
            return -1
        # 1 . build graph
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # 2. dfs
        visited = [False]*n

        def bfs(node):            
            q = collections.deque([node])
            while q:
                current_node = q.popleft()

                # go through all the neighbors
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        # 3. count the number of connected components
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)

        # 4. return the number of connected components - 1
        return count - 1

# Switch to wireless technology to avoid such type of problems in life
if __name__ == "__main__":
    n = 4
    connections = [[0, 1], [0, 2], [1, 2]]
    print(Solution().makeConnected(n, connections))
