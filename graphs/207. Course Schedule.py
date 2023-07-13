"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The Logic to to find the cycle in the graph 
        # if cycle then return False
        # else return True

        # 0 - unvisited
        # 1 - visiting
        # 2 - visited

        # Create a graph

        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[course].append(pre)


        visited = [0] * numCourses


        for i in range(numCourses):
            if self.dfs(graph, visited, i):
                return False
            

        return True
    

    def dfs(self, graph, visited, i):
        # if node is currently being visited, cycle is detected, not safe
        if visited[i] == 1:
            return True
        

        # if node has been visited and marked safe, return True
        if visited[i] == 2:
            return False
        
        # Mark node as visiting
        visited[i] = 1

        # Explore neighbors of the current node

        for nei in graph[i]:
            if self.dfs(graph, visited, nei):
                return True
            

        # Mark node as visited and safe
        visited[i] = 2

        return False
    
# Big o analysis
# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges

# Space complexity: O(V) where V is the number of vertices


    
s = Solution()
print(s.canFinish(2, [[1,0]]))