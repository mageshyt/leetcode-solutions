"""
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:


Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.
"""


from typing import List
from collections import defaultdict
import heapq
from math import ceil, floor
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_graph(edges):
            graph=defaultdict(list)
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        adj1=build_graph(edges1)
        adj2=build_graph(edges2)


        def get_diameter(curr,par,adj):
            max_distance=0
            max_chid_paths=[0,0] # [left,right]

            for nei in adj[curr]:
                if nei == par:
                    continue
                nei_distance,nei_max_leaf=get_diameter(nei,curr,adj)

                heapq.heappush(max_chid_paths,nei_max_leaf)
                heapq.heappop(max_chid_paths)

                max_distance=max(max_distance,nei_distance)
            max_distance=max(max_distance,sum(max_chid_paths))
            return max_distance, max(max_chid_paths)+1

        diameter1,_=get_diameter(0,-1,adj1)
        diameter2,_=get_diameter(0,-1,adj2)

        return max(diameter1,diameter2,1+ceil(diameter1/2)+ceil(diameter2/2))


edges1 = [[0,1],[0,2],[0,3]]
edges2 = [[0,1]]
print(Solution().minimumDiameterAfterMerge(edges1, edges2)) # 3

