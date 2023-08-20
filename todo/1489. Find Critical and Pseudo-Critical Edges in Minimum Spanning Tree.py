


# Union Find Template

class UnionFind:
    
    def __init__(self) -> None:
        self.UF = {}
 
    def find(self, x):
        self.UF.setdefault(x, x)  # Initialize a new set for x if not present
        if x != self.UF[x]:
            self.UF[x] = self.find(self.UF[x])  # Path compression: Find the ultimate parent of x
        return self.UF[x]
    
    def union(self, x, y):
        self.UF[self.find(x)] = self.find(y)  # Merge two sets by making y's parent as x's parent

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        def cmp(a, b):
            return a[2] < b[2]

        for i, e in enumerate(edges):
            e.append(i)  # Append the original index to the edge for sorting later

        edges.sort(key=lambda x: x[2])  # Sort edges by weight

        # Find the minimum spanning tree (MST) weight
        mst_weight = self.find_mst(n, edges, -1, -1)

        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            # Check if removing this edge increases the MST weight (critical edge)
            if self.find_mst(n, edges, i, -1) > mst_weight:
                critical.append(edges[i][3])
            # Check if including this edge results in the same MST weight (pseudo-critical edge)
            elif self.find_mst(n, edges, -1, i) == mst_weight:
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]
 
    def find_mst(self, n, edges, block, e):
        uf = UnionFind()  # Create a new instance of the UnionFind class
        weight = 0
        
        if e != -1:
            weight += edges[e][2]  # Add the weight of the specified edge
            uf.union(edges[e][0], edges[e][1])  # Union the vertices of the edge
        
        for i in range(len(edges)):
            if i == block:
                continue
            if uf.find(edges[i][0]) == uf.find(edges[i][1]):
                continue
            uf.union(edges[i][0], edges[i][1])  # Union vertices of the current edge
            weight += edges[i][2]  # Add the weight of the current edge to the MST weight
        
        for i in range(n):
            if uf.find(i) != uf.find(0):  # Check if all vertices are in the same set (connected)
                return float('inf')  # If not, return infinity to indicate disconnected graph
        
        return weight  # Return the MST weight
 

if __name__ == "__main__":
    s=Solution()
    n = 5
    roads =  [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    print("res",s.findCriticalAndPseudoCriticalEdges(n,roads))