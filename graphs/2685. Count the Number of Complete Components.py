"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
 


"""

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x) # initialize the parent of the node to itself

        if x != self.parent[x]: # if the node is not the parent of itself
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x] # return the parent of the node


    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)


from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf=UnionFind()

        # make the graph
        for u,v in edges:
            uf.union(u,v)

        count=0

        components_vertices={}
        components_edges={}

        for i in range(n):
            root=uf.find(i)
            if root not in components_vertices:
                components_vertices[root]=set()
                components_edges[root]=0

            components_vertices[root].add(i)

        for u,v in edges:
            root=uf.find(u)
            components_edges[root]+=1

        for root in components_vertices:
            num_vertices=len(components_vertices[root])
            need_edges= num_vertices*(num_vertices-1)//2

            if need_edges==components_edges[root]:
                count+=1

        return count

print(Solution().countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]])) #3


