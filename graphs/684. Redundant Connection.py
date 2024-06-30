"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1] * (len(edges)+1)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            rootx=find(x) # find the parent of x
            rooty=find(y) # find the parent of y
            if rootx!=rooty: #
                if rank[rootx]>rank[rooty]:
                    parent[rooty]=rootx
                elif rank[rootx]<rank[rooty]:
                    parent[rootx]=rooty
                else:
                    parent[rooty]=rootx
                    rank[rootx]+=1



        for edge in edges:
            if find(edge[0])==find(edge[1]):
                return edge
            union(edge[0],edge[1])

if __name__ == "__main__":
    print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]])) # [2,3]

    print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1,4]