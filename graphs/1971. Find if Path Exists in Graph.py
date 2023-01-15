'''There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.'''


class Solution:
    def validPath(self, n: int, edges, source: int, destination: int):
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        visited = [False] * n
        queue = [source]
        while queue:
            node = queue.pop(0)
            visited[node] = True
            if node == destination:
                return True
                
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
        return False


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 8
    print(Solution().validPath(n, edges, source, destination))
