"""
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:



After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.
"""
from typing import List
from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj=[[i+1] for i in range(n)] # adjacency list
        
        
        def bfs():
            q=deque([(0,0)]) # node, distance
            visited=set()

            while q:
                node, distance=q.popleft()
                if node == n-1:
                    return distance

                for neighbor in adj[node]:
                    if neighbor not in visited:
                        q.append((neighbor,distance+1))
                        visited.add(neighbor)



        result=[]

        for u,v in queries:
            adj[u].append(v)
            result.append(bfs())

        return result

n = 5
queries = [[2,4],[0,2],[0,4]]

print(Solution().shortestDistanceAfterQueries(n, queries)) # [3,2,1]
