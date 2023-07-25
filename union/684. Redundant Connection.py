class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        UF={}

        def find(x):
            UF.setdefault(x,x)
            if x!=UF[x]:
                UF[x]=find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF[find(x)]=find(y)

        for x,y in edges:
            if find(x)==find(y):
                return [x,y]
            union(x,y)

