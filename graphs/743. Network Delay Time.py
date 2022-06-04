'''You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1'''

import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        # create adj list
        adj=collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        total_time=0
        # create a set of visited nodes
        visited=set()
        #min head
        min_heap= [(0,k)]
        while min_heap:
            #pop the min node
            time,node=heapq.heappop(min_heap)
            # if node is already visited, continue
            if node in visited:continue
            # add to visited
            visited.add(node)
            # add to total time
            total_time=max(total_time,time)
            # add all the neighbors to min heap
            for neighbor,weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap,(time+weight,neighbor))
        # if all nodes are visited, return total time
        return total_time if len(visited)==n else -1


if __name__=='__main__':
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    print(Solution().networkDelayTime(times, n, k))
