"""There is an infrastructure of n cities with some number of roads connecting these cities. 
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

"""
from collections import defaultdict
from typing import List
import itertools

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Create a defaultdict to store the adjacency list representation of the graph
        graph = defaultdict(set)

        # Populate the graph based on the given roads
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)

        max_rank = 0

        # Iterate through all pairs of cities
        for city1, city2 in itertools.combinations(range(n), 2):
            # Check if there is a direct road between city1 and city2
            has_road = 1 if city2 in graph[city1] else 0

            # Calculate the rank of the network for this pair of cities
            road_length = len(graph[city1]) + len(graph[city2]) - has_road
            print(city1,city2,road_length,max_rank)

            # Update the maximum rank if the current rank is higher
            max_rank = max(max_rank, road_length)

        return max_rank
    
        # Time complexity: O(n^2)
        # Space complexity: O(n)

        # solution 2

    def maximalNetworkRank2(self,n,roads):
        # connections
        connections = [0] * n

        # build the graph

        graph = defaultdict(set)

        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
            connections[city1] += 1
            connections[city2] += 1

        # find the max rank

        max_rank = 0

        for i in range(n):
            for j in range(i+1,n):
                rank = connections[i] + connections[j]
                
                if j in graph[i]:
                    rank -= 1
                max_rank = max(max_rank,rank)


if __name__ == "__main__":
    s=Solution()
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    print(s.maximalNetworkRank(n,roads))

