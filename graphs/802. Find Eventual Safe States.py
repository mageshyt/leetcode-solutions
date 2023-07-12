"""There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order."""

from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0 - unvisited
        # 1 - visiting
        # 2 - visited
        visited = [0] * len(graph)  # Initialize all nodes as unvisited
        res = []  # List to store eventual safe nodes
        
        for i in range(len(graph)):
            if self.dfs(graph, visited, i):  # Perform depth-first search for each node
                res.append(i)  # If node is eventually safe, add it to the result list
        
        return res
    
    def dfs(self, graph, visited, i):
        if visited[i] == 1:  # If node is currently being visited, cycle is detected, not safe
            return False
        if visited[i] == 2:  # If node has been visited and marked safe, return True
            return True
        
        visited[i] = 1  # Mark node as visiting
        
        for j in graph[i]:  # Explore neighbors of the current node
            if not self.dfs(graph, visited, j):  # If any neighbor is not safe, return False
                return False
        
        visited[i] = 2  # Mark node as visited and safe
        return True

