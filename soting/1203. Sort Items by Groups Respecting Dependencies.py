"""1203. Sort Items by Groups Respecting Dependencies
Hard
1.2K
204
Companies
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
"""

from typing import Dict, List
from collections import deque, defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Sort items considering groups and dependencies.
        
        Args:
            n (int): The number of items.
            m (int): The number of groups.
            group (List[int]): List of group assignments for each item.
            beforeItems (List[List[int]]): Dependencies of each item.
        
        Returns:
            List[int]: Sorted list of items based on group dependencies.
        """
        
        # Step 1: Assign groups to items with -1 group
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        # Step 2: Build the dependency graph for items and groups
        item_graph = defaultdict(list)  # Dependency graph for items
        group_graph = defaultdict(list)  # Dependency graph for groups
        
        # Calculate in-degrees for items and groups
        item_indegree = [0] * n  # In-degrees for items
        group_indegree = [0] * group_id  # In-degrees for groups
        
        for i in range(n):
            for prev in beforeItems[i]:
                # Build item dependency graph and calculate in-degrees
                item_graph[prev].append(i)
                item_indegree[i] += 1
                
                if group[prev] != group[i]:
                    # Build group dependency graph and calculate in-degrees
                    group_graph[group[prev]].append(group[i])
                    group_indegree[group[i]] += 1
        
        # Step 3: Perform topological sorting to solve the problem
        item_order = self.topologicalSort(item_graph, item_indegree)
        group_order = self.topologicalSort(group_graph, group_indegree)
        
        # Check if there are cycles in the graphs
        if not item_order or not group_order:
            return []
        
        # Organize items based on their groups
        item_to_group = defaultdict(list)
        
        for item in item_order:
            item_to_group[group[item]].append(item)
        
        sorted_items = []
        
        # Construct the sorted list of items based on group order
        for group in group_order:
            sorted_items.extend(item_to_group[group])
        
        return sorted_items
    
    def topologicalSort(self, graph: Dict[int, List[int]], indegree: List[int]):
        """
        Perform topological sorting on a graph.
        
        Args:
            graph (Dict[int, List[int]]): Dependency graph.
            indegree (List[int]): List of in-degrees for each node.
        
        Returns:
            List[int]: Topologically sorted nodes.
        """
        visited = []
        queue = deque()
        
        # Initialize the queue with nodes having zero in-degree
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        # Perform topological sorting using BFS
        while queue:
            top = queue.popleft()
            visited.append(top)
            
            # Reduce the in-degree of neighboring nodes
            for neighbor in graph[top]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all nodes were visited, there is a cycle
        return visited if len(visited) == len(graph) else []

 
if __name__ == "__main__":
    n = 8
    m = 2
    group = [-1,-1,1,0,0,1,0,-1]
    beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    print(Solution().sortItems(n, m, group, beforeItems))