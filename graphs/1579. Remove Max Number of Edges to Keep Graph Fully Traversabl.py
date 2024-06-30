
from typing import List
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = n
        self.rank=[1] * (n+1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.size -= 1
        return True

    def isConnect(self):
        return self.size==1


class Solution:
    # Time complexity: O(nlogn) | Space complexity: O(n)
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # base template for union find
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        # 0: common edge, 1: Alice, 2: Bob, 3: both

        parent = [i for i in range(n+1)]
        # sort edges by type
        edges.sort(key=lambda x: -x[0])
        res = 0

        for t, u, v in edges:
            # t=3 is common edge
            if t == 3:
                if not union(u, v):
                    res += 1
        parentA = parent[:]
        parentB = parent[:]
        for t, u, v in edges:
            if t == 1:
                if not union(u, v):
                    res += 1
        if len(set(find(i) for i in range(1, n+1))) > 1:
            return -1
        parent = parentA
        for t, u, v in edges:
            if t == 2:
                if not union(u, v):
                    res += 1
        if len(set(find(i) for i in range(1, n+1))) > 1:
            return -1
        return res

    # Time complexity: O(n) | Space complexity: O(n)

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n) # create two union find objects

        res = 0
        for t, src, des in edges:
            if t == 3:
                res+=(alice.union(src, des) | bob.union(src, des))

        for t, src, des in edges:
            # alice part
            if t == 1:
                res += alice.union(src, des)

            # bob part
            if t == 2:
                res += bob.union(src, des)


        if alice.isConnect() and bob.isConnect():
            return len(edges) - res

        return -1





print(Solution().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])) # 2
print(Solution().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])) # 0
