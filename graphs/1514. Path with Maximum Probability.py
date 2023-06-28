
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

 

        # we use djikstra's algorithm to find the shortest path from start to end
        # we use a heap to store the nodes that we have visited

        adj=defaultdict(list)

        for i in range(len(edges)):
            src,dest=edges[i]

            adj[src].append((dest,succProb[i]))

            adj[dest].append((src,succProb[i]))


        visited=set()


        heap = [] # (prob,node)
        heapq.heappush(heap,(-1,start)) # we use -1 to represent 1.0 probability

        while heap:
            prop,parent=heapq.heappop(heap)

            visited.add(parent) # we add the node to visited
            if parent==end: # if we reach the end, we return the probability
                return -prop
            
            for child,childProb in adj[parent]:

                if child not in visited:
                    totalProb=prop*childProb
                    heapq.heappush(heap,(totalProb,child))

        return 0



if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    s = Solution()
    print(s.maxProbability(n,edges,succProb,start,end))