from typing import List
class Solution:
    # topo
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDegree=[0]*n

        for u,v in edges:
            inDegree[v]+=1


        chaps=[i for i in range(n) if inDegree[i]==0]


        return chaps[0] if len(chaps)==1 else -1

n = 3
edges = [[0,1],[1,2]]

print(Solution().findChampion(n, edges)) # 0
