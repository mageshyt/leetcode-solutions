class Solution:
    def minCostConnectPoints(self, points) :
        length = len(points)
        # Create an adjacency list to represent the graph, where each point is a node and the edge weight is the distance between points.
        adj = {i: [] for i in range(length)}
        
        # Create edges based on the Manhattan distance between points and populate the adjacency list.
        for i in range(length):
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                # Calculate the Manhattan distance between the points.
                dist = abs(x1 - x2) + abs(y1 - y2)
                # Add the distance and the neighboring point to the adjacency list for both points.
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        # Initialize variables for minimum cost and visited nodes.
        min_cost = 0
        visited = set()
        # Initialize a min heap to keep track of the edges.
        heap = [[0, 0]]
        
        # Implement Prim's algorithm to find the minimum cost spanning tree.
        while len(visited) < length:
            cost, node = heapq.heappop(heap)
            if node in visited:
                # If the node is already visited, skip it.
                continue
            
            min_cost += cost
            visited.add(node)
            
            # Explore neighboring nodes and add the edges to the min heap.
            for cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, [cost, nei])
        
        return min_cost
