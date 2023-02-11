"""You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]"""


import collections


class Solution:

    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):

        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for src, dest in redEdges:
            red[src].append(dest)  # red edge from src to dest

        for src, dest in blueEdges:
            blue[src].append(dest)

        # res
        res = [-1] * n
        # BFS

        res[0] = 0  # it is the starting point so distance is 0
        q = collections.deque()

        q.append((0, 0, None))  # node, distance, color

        visited = set()
        visited.add((0, None))

        print(red, blue)

        while q:

            node, dist, color = q.popleft()
            print('node, dist, color', node, dist, color)

            # if we visit a node first time
            if res[node] == -1:
                res[node] = dist  # update the distance

            # if color is not read then go to red neighbors

            if color != 'red':
                for child in red[node]:
                    if (child, 'red') not in visited:
                        q.append((child, dist + 1, 'red'))  # add to queue
                        visited.add((child, 'red'))  # mark as visited

            if color != 'blue':
                for child in blue[node]:  # if color is not blue then go to blue neighbors
                    if (child, 'blue') not in visited:
                        q.append((child, dist + 1, 'blue'))  # add to queue
                        visited.add((child, 'blue'))  # mark as visited

        return res


if __name__ == '__main__':
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))