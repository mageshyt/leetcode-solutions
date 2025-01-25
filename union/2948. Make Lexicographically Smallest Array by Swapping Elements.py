
from typing import List
from collections import defaultdict as DefaultDict
from collections import deque as Deque

class UnionFind:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: int) -> int:
        self.parent.setdefault(x, x) # initialize the parent of the node to itself

        if x != self.parent[x]: # if the node is not the parent of itself
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x] # return the parent of the node


    def union(self, x: int, y: int) -> None:

        xParent = self.find(x)
        yParent = self.find(y)

        if xParent != yParent:
            self.parent[xParent] = yParent

    def is_connected(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        uf = UnionFind()
        n = len(sorted_nums)
        
        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] <= limit:
                uf.union(sorted_nums[i], sorted_nums[i - 1])

        graph = DefaultDict(Deque)
        for num in sorted_nums:
            graph[uf.find(num)].append(num)

        res = []
        for num in nums:  # Use the original array
            res.append(graph[uf.find(num)].popleft())
        
        return res

sol = Solution()


print(sol.lexicographicallySmallestArray([3,6,9,1], 2)) # [1,3,6,9]
print(sol.lexicographicallySmallestArray([1,7,6,18,2,1], 3)) # [1,3,6,9]
