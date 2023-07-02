from typing import List
import itertools
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for k in range(len(requests),0,-1):

            for  i in  itertools.combinations(range(len(requests)),k):

                deg=[0]*n # degree of each node [indegree-outdegree]

                for j in i:

                    deg[requests[j][0]]-=1
                    deg[requests[j][1]]+=1


                if all([d==0 for d in deg]):
                    return k
                

        return 0
    
# 1. we will try to make all the nodes have 0 degree
# 2. we will try to make the incoming and outgoing edges equal


req=[[1,1],[1,0],[0,1],[0,0],[0,0],[0,1],[0,1],[1,0],[1,0],[1,1],[0,0],[1,0]]

print(Solution().maximumRequests(2,req))

        